# ---------------------------
# Import Stuff Here
# ---------------------------
import requests
from bs4 import BeautifulSoup
import pandas as pd
import pathlib

def find_col():
    info = requests.get(f'https://www.thestar.com.my/Business/Marketwatch/Stocks?qcounter=NESTLE')
    parser = BeautifulSoup(info.text, 'html.parser')
    
    table_columns = parser.find('thead',{"class":"market-trans-head"})
    table_columns = table_columns.find_all('td')
    
    df_columns = []
    for each in table_columns:
        #print(each.get_text())
        df_columns.append(each.get_text())
    df_columns.append('Date')
    return(df_columns)
    
def find_data(stocks):
    df_contents = []
    for ident in enumerate(stocks):
        try:
            info = requests.get(f'https://www.thestar.com.my/Business/Marketwatch/Stocks?qcounter={ident[1]}')
            parser = BeautifulSoup(info.text, 'html.parser')
            
            table_contents = parser.find('tbody')
            table_contents = table_contents.find_all('td')

            temp = []
            for each in table_contents:
                #print(each.get_text())
                temp.append(each.get_text())
                
            d = parser.find("p").find('span').get_text()
            temp.append(d)

            df_contents.append(temp)
        except:
            print(ident[1],'not found')
            df_contents.append('Empty List')
    return(df_contents)

def filer(df):
    try:
        csv = df.to_csv()
        w = open(f'{pathlib.Path(__file__).parent}\prices.csv','a')
        w.write(csv)
        w.close()
    except:
        print('Error when writing file, make sure it\'s not open in another program')
        
r = open(f'{pathlib.Path(__file__).parent}\params.txt','r')
stocks = eval(r.read())
#stocks = ['GENM', 'GENTING', 'CIMB', 'MAYBANK', 'PBBANK', 'NESTLE', 'TOPGLOV', 'SUNREIT', 'EWINT', 'PAVREIT', 'IGBREIT', 'KLCC']
df = pd.DataFrame(data = find_data(stocks), columns=find_col())
df.index = stocks

filer(df)