import streamlit as st
import pandas as pd

# Title
st.title("Sales Data Analysis Dashboard")

# Load CSV file
df = pd.read_csv("sales_data.csv")

# Display Data
st.subheader("Sales Data")
st.dataframe(df)

# Total Sales
total_sales = df["Sales"].sum()
st.write("### Total Sales:", total_sales)

# Total Profit
total_profit = df["Profit"].sum()
st.write("### Total Profit:", total_profit)

# Sales by Category
st.subheader("Sales by Category")
category_sales = df.groupby("Category")["Sales"].sum()
st.bar_chart(category_sales)

# Profit by Region
st.subheader("Profit by Region")
region_profit = df.groupby("Region")["Profit"].sum()
st.bar_chart(region_profit)