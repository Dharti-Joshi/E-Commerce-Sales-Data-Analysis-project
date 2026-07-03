from data_cleaning import clean_data

def load_data():
    df = clean_data("ecommerce_sales.csv")

    if df is not None:
        print("Data loaded successfully!")
        return df
    else:
        print("Loading failed")
        return None