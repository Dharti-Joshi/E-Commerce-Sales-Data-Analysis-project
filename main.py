import pandas as pd

# CSV file load
df = pd.read_csv("ecommerce_sales.csv")

print("="*40)
print("E-COMMERCE DATA ANALYSIS")
print("="*40)

# Show data
print("\nDATA:")
print(df)

# Total Orders
print("\nTotal Orders:", len(df))

# Total Sales
total_sales = df["Total_Sales"].sum()
print("Total Sales:", total_sales)

# Average Sales
avg_sales = df["Total_Sales"].mean()
print("Average Order Value:", avg_sales)

# Top Product by Quantity
top_product = df.groupby("Product_Name")["Quantity"].sum().sort_values(ascending=False)
print("\nTop Products:")
print(top_product)

# Category wise sales
category_sales = df.groupby("Category")["Total_Sales"].sum()
print("\nCategory Wise Sales:")
print(category_sales)

# Payment method count
print("\nPayment Methods:")
print(df["Payment_Method"].value_counts())

# Order status count
print("\nOrder Status:")
print(df["Order_Status"].value_counts())

from data_loader import load_data

df = load_data()

print(df.head())
import pandas as pd
from visualization import visualize_data

# Load CSV
df = pd.read_csv("ecommerce_sales.csv")

print("=" * 50)
print("        E-COMMERCE SALES DATA ANALYSIS")
print("=" * 50)

# Display first 5 rows
print("\nFirst 5 Records:")
print(df.head())

# Total Orders
print("\nTotal Orders:", len(df))

# Total Sales
print("Total Sales:", df["Total_Sales"].sum())

# Average Sales
print("Average Order Value:", round(df["Total_Sales"].mean(), 2))

# Top Products
print("\nTop Selling Products:")
print(df.groupby("Product_Name")["Quantity"].sum().sort_values(ascending=False))

# Category-wise Sales
print("\nCategory Wise Sales:")
print(df.groupby("Category")["Total_Sales"].sum())

# Payment Methods
print("\nPayment Methods:")
print(df["Payment_Method"].value_counts())

# Order Status
print("\nOrder Status:")
print(df["Order_Status"].value_counts())

# Call Visualization Function
visualize_data(df)

print("\nAnalysis Completed Successfully!")