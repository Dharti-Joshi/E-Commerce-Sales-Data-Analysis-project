def product_analysis(df):

    print("\n===== PRODUCT ANALYSIS =====")

    # 1. Top selling products (by quantity)
    print("\nTop Selling Products (by Quantity):")
    print(df.groupby("Product_Name")["Quantity"].sum().sort_values(ascending=False))

    # 2. Product wise revenue
    print("\nProduct Wise Revenue:")
    print(df.groupby("Product_Name")["Total_Sales"].sum().sort_values(ascending=False))

    # 3. Category wise product performance
    print("\nCategory Wise Sales:")
    print(df.groupby("Category")["Total_Sales"].sum())

    # 4. Average price per product
    print("\nAverage Price per Product:")
    print(df.groupby("Product_Name")["Unit_Price"].mean())

    print("\n===== PRODUCT ANALYSIS COMPLETED =====")