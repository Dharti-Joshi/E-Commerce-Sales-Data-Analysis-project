import matplotlib.pyplot as plt
import seaborn as sns

def visualize_data(df):

    print("\n===== VISUALIZATION STARTED =====")

    # Style
    sns.set(style="whitegrid")

    # 1. Category wise sales (Bar chart)
    plt.figure(figsize=(8,5))
    category_sales = df.groupby("Category")["Total_Sales"].sum()
    category_sales.plot(kind="bar", color="skyblue")
    plt.title("Category Wise Sales")
    plt.xlabel("Category")
    plt.ylabel("Total Sales")
    plt.tight_layout()
    plt.show()

    # 2. Payment method distribution (Pie chart)
    plt.figure(figsize=(6,6))
    payment = df["Payment_Method"].value_counts()
    plt.pie(payment, labels=payment.index, autopct="%1.1f%%")
    plt.title("Payment Method Distribution")
    plt.show()

    # 3. Top products (Bar chart)
    plt.figure(figsize=(8,5))
    top_products = df.groupby("Product_Name")["Quantity"].sum()
    top_products.sort_values(ascending=False).plot(kind="bar", color="green")
    plt.title("Top Selling Products")
    plt.xlabel("Product")
    plt.ylabel("Quantity Sold")
    plt.tight_layout()
    plt.show()

    print("===== VISUALIZATION COMPLETED =====")