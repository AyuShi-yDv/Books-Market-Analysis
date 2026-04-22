import streamlit as st
import pandas as pd

st.set_page_config(page_title="Product Dashboard", layout="wide")

st.title("📊 Product Insights Dashboard")

df = pd.read_csv("data.csv")

# Filters
price_filter = st.slider("Select Max Price", 0, int(df["Price"].max()), 50)

filtered = df[df["Price"] <= price_filter]

# Metrics
col1, col2 = st.columns(2)
col1.metric("Total Products", len(filtered))
col2.metric("Average Price", round(filtered["Price"].mean(), 2))

# Table
st.subheader("📄 Product Data")
st.dataframe(filtered)

# Chart
st.subheader("📊 Price Distribution")
st.bar_chart(filtered["Price"])