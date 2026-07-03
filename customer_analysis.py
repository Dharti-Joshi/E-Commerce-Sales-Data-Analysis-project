def customer_analysis(df):

    print("\n===== CUSTOMER ANALYSIS =====")

    # 1. Top customers by total spending
    top_customers = df.groupby("Customer_Name")["Total_Sales"].sum().sort_values(ascending=False)
    print("\nTop Customers (by " \
    "spending):")
    print(top_customers)

    # 2. Total unique customers
    print("\nTotal Unique Customers:", df["Customer_Name"].nunique())

    # 3. Average order value per customer
    avg_order = df.groupby("Customer_Name")["Total_Sales"].mean().sort_values(ascending=False)
    print("\nAverage Order Value per Customer:")
    print(avg_order)

    # 4. Number of orders per customer
    order_count = df["Customer_Name"].value_counts()
    print("\nNumber of Orders per Customer:")
    print(order_count)

    print("\n===== CUSTOMER ANALYSIS COMPLETED =====")