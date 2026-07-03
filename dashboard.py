import streamlit as st
import pandas as pd

# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(
    page_title="E-Commerce Dashboard",
    layout="wide",
    initial_sidebar_state="collapsed"
)
st.title("🛒 E-Commerce Sales Dashboard")
st.write("Python + Streamlit Data Analysis Project")

# ----------------------------
# Load Data
# ----------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("ecommerce_sales.csv")

    # Safe date conversion
    df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")

    return df

df = load_data()

# ----------------------------
# Sidebar Filters
# ----------------------------
st.sidebar.header("🔍 Filters")

category = st.sidebar.selectbox(
    "Category",
    ["All"] + list(df["Category"].dropna().unique())
)

city = st.sidebar.selectbox(
    "City",
    ["All"] + list(df["City"].dropna().unique())
)

payment = st.sidebar.selectbox(
    "Payment Method",
    ["All"] + list(df["Payment_Method"].dropna().unique())
)

# ----------------------------
# Apply Filters
# ----------------------------
filtered_df = df.copy()

if category != "All":
    filtered_df = filtered_df[filtered_df["Category"] == category]

if city != "All":
    filtered_df = filtered_df[filtered_df["City"] == city]

if payment != "All":
    filtered_df = filtered_df[filtered_df["Payment_Method"] == payment]

# ----------------------------
# Safe Metrics
# ----------------------------
total_orders = len(filtered_df)
total_sales = filtered_df["Total_Sales"].sum() if len(filtered_df) > 0 else 0
avg_sales = filtered_df["Total_Sales"].mean() if len(filtered_df) > 0 else 0
total_qty = filtered_df["Quantity"].sum() if len(filtered_df) > 0 else 0

# ----------------------------
# KPI Cards
# ----------------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("📦 Orders", total_orders)
col2.metric("💰 Sales", f"₹ {total_sales:,.2f}")
col3.metric("📊 Avg Sales", f"₹ {avg_sales:,.2f}")
col4.metric("🛍 Quantity", total_qty)

st.markdown("---")

# ----------------------------
# Dataset
# ----------------------------
st.subheader("📄 Data Preview")
st.dataframe(filtered_df)

# ----------------------------
# Category Wise Sales
# ----------------------------
st.subheader("📊 Category Wise Sales")
st.bar_chart(filtered_df.groupby("Category")["Total_Sales"].sum())

# ----------------------------
# Top Products
# ----------------------------
st.subheader("🏆 Top Products")
st.bar_chart(
    filtered_df.groupby("Product_Name")["Quantity"]
    .sum()
    .sort_values(ascending=False)
)

# ----------------------------
# City Wise Sales
# ----------------------------
st.subheader("🏙 City Wise Sales")
st.bar_chart(filtered_df.groupby("City")["Total_Sales"].sum())

# ----------------------------
# Payment Method
# ----------------------------
st.subheader("💳 Payment Methods")
st.bar_chart(filtered_df["Payment_Method"].value_counts())

# ----------------------------
# Order Status
# ----------------------------
st.subheader("🚚 Order Status")
st.bar_chart(filtered_df["Order_Status"].value_counts())

# ----------------------------
# Sales Trend
# ----------------------------
st.subheader("📈 Daily Sales Trend")

if len(filtered_df) > 0:
    st.line_chart(filtered_df.groupby("Order_Date")["Total_Sales"].sum())

# ----------------------------
# Download Button
# ----------------------------
st.download_button(
    label="📥 Download Data",
    data=filtered_df.to_csv(index=False),
    file_name="filtered_sales.csv",
    mime="text/csv"
)
#python -m streamlit run dashboard.py


