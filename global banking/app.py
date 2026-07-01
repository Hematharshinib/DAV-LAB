import streamlit as st
import pandas as pd
import plotly.express as px

# Page Configuration
st.set_page_config(page_title="Global Banking Data Analytics", layout="wide")

st.title("🏦 Global Banking Data Analytics & Visualization")

# Load Dataset
df = pd.read_csv("banking_data.csv")

# Sidebar Filters
st.sidebar.header("Filters")

country = st.sidebar.multiselect(
    "Select Country",
    options=df["Country"].unique(),
    default=df["Country"].unique()
)

account = st.sidebar.multiselect(
    "Select Account Type",
    options=df["AccountType"].unique(),
    default=df["AccountType"].unique()
)

filtered_df = df[
    (df["Country"].isin(country)) &
    (df["AccountType"].isin(account))
]

# KPI Cards
total_customers = len(filtered_df)
total_balance = filtered_df["Balance"].sum()
avg_credit = filtered_df["CreditScore"].mean()

col1, col2, col3 = st.columns(3)

col1.metric("👥 Customers", total_customers)
col2.metric("💰 Total Balance", f"${total_balance:,.0f}")
col3.metric("⭐ Avg Credit Score", f"{avg_credit:.0f}")

st.markdown("---")

# Charts
col4, col5 = st.columns(2)

with col4:
    st.subheader("Balance by Country")

    country_balance = (
        filtered_df.groupby("Country")["Balance"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        country_balance,
        x="Country",
        y="Balance",
        color="Country",
        text_auto=True
    )

    st.plotly_chart(fig, use_container_width=True)

with col5:
    st.subheader("Account Type Distribution")

    fig2 = px.pie(
        filtered_df,
        names="AccountType",
        hole=0.4
    )

    st.plotly_chart(fig2, use_container_width=True)

st.subheader("Loan Amount by Customer")

fig3 = px.line(
    filtered_df,
    x="CustomerID",
    y="LoanAmount",
    markers=True
)

st.plotly_chart(fig3, use_container_width=True)

st.subheader("Income vs Credit Score")

fig4 = px.scatter(
    filtered_df,
    x="Income",
    y="CreditScore",
    color="Country",
    size="Balance"
)

st.plotly_chart(fig4, use_container_width=True)

st.subheader("Banking Data")

st.dataframe(filtered_df, use_container_width=True)

csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    "📥 Download Filtered Data",
    csv,
    "banking_data.csv",
    "text/csv"
)