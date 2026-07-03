import pandas as pd

def clean_data(file_name):
    df = pd.read_csv(file_name)

    df.columns = df.columns.str.strip()
    df.drop_duplicates(inplace=True)

    print("Data cleaned successfully!")

    return df