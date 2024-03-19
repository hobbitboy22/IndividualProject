import csv
from Compare_Headers_Test import compare_csv_formats

data = 'Data.csv'
alt = 'testdata.csv'

if(compare_csv_formats(data, alt)):
    print("Same format")
else:
    print("The given files are not the same format")    