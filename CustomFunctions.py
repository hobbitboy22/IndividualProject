import pandas as pd

data = pd.read_csv('Data.csv')

def get_csv_headers(file_path):
    data = pd.read_csv(file_path, nrows = 1)
    headers = data.columns.tolist()
    return headers

def compare_csv_formats(main, alt):
    main_headers = main.columns.tolist() if isinstance(main, pd.DataFrame) else get_csv_headers(main)
    alt_headers = alt.columns.tolist() if isinstance(alt, pd.DataFrame) else get_csv_headers(alt)
    return main_headers == alt_headers
    
def get_unique_values(csv, value):
    uniqueValue = csv[value].unique()
    print(uniqueValue)
    return uniqueValue