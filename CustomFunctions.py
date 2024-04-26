import pandas as pd
import csv
import os

data = pd.read_csv('Data.csv')
data2 = pd.read_csv('BaseData.csv')

filepath = os.path.abspath('BaseData.csv')

# Function to get the headers of a csv file
def get_csv_headers(file_path):
    data = pd.read_csv(file_path, nrows = 1)
    headers = data.columns.tolist()
    return headers

# Function to compare the headers of 2 seperate csv files
def compare_csv_formats(main, alt):
    # Allows the user to use both datasets and csv files without causing an error
    main_headers = main.columns.tolist() if isinstance(main, pd.DataFrame) else get_csv_headers(main)
    alt_headers = alt.columns.tolist() if isinstance(alt, pd.DataFrame) else get_csv_headers(alt)
    return main_headers == alt_headers
    
# Function to get the all of the unique values of a specific row
def get_unique_values(csvfile, value):
    uniqueValue = csvfile[value].unique()
    return uniqueValue

# Function to add the given data to a given csv file
def add_data(csvfile, NewData):
    with open(filepath, 'a', newline = '') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(NewData)