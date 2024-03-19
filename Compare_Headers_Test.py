import pandas as pd

def get_csv_headers(file_path):
    data = pd.read_csv(file_path, nrows = 1)
    headers = data.columns.tolist()
    return headers

def compare_csv_formats(main, alt):
    main_headers = main.columns.tolist() if isinstance(main, pd.DataFrame) else get_csv_headers(main)
    alt_headers = alt.columns.tolist() if isinstance(alt, pd.DataFrame) else get_csv_headers(alt)
    return main_headers == alt_headers

data_csv = pd.read_csv('Data.csv')
alt_csv = pd.read_csv('testdata.csv')

print(compare_csv_formats(data_csv, alt_csv))