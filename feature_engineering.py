import pandas as pd

def feature_engineering(df):

    df = df.copy()

    df["Total_Revenue"] = df["Quantity"] * df["Unit_Price"]

    df["Discount_Amount"] = (df["Total_Revenue"] * df["Discount"]) / 100

    df["Final_Sale"] = df["Total_Revenue"] - df["Discount_Amount"]

    df["Order_Date"] = pd.to_datetime(df["Order_Date"])
    df["Month"] = df["Order_Date"].dt.month

    df["Day_Name"] = df["Order_Date"].dt.day_name()

    df["High_Value_Order"] = df["Final_Sale"].apply(
        lambda x: "Yes" if x > 5000 else "No"
    )

    print("Feature Engineering completed successfully!")

    return df