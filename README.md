# A Smol' Task

## [0.1]
Simple program to return all target stocks data from the star website. Still a WIP, will have more features in future.
For now, just run the program and a csv file will be created.

It will overwrite previous data in csv, I am working on fixing it but please dont accidentally write over your old data.

## [0.2]
Fixed issue with overwriting and added a function to read from text file in same folder called params.txt.
In future will add interactive file selection and GUI.

you will need these modules:
- pathlib
- pandas
- bs4
- requests
