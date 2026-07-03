def sales_analysis(df):

    print("SALES ANALYSIS STARTED")

    print("Total Sales:", df["Total_Sales"].sum())

    print("\nCategory Wise Sales:")
    print(df.groupby("Category")["Total_Sales"].sum())

    print("\nTop Products:")
    print(df.groupby("Product_Name")["Quantity"].sum())

    print("\nPayment Methods:")
    print(df["Payment_Method"].value_counts())

    print("\nOrder Status:")
    print(df["Order_Status"].value_counts())
    import pandas as pd

df = pd.read_csv("ecommerce_sales.csv")
 📊 KPI (Key Performance Indicators)

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order ID"].nunique()
avg_order_value = df["Sales"].mean()

print("📊 KPI REPORT")
print("----------------------")
print("Total Sales:", total_sales)
print("Total Profit:", total_profit)
print("Total Orders:", total_orders)
print("Average Order Value:", avg_order_value)