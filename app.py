import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

st.set_page_config(page_title="Product Dashboard", layout="wide")

# ======================
# TITLE + INTRO
# ======================
st.title("📚 Books Market Analysis Dashboard")

st.markdown("""
### 🎯 Objective  
Analyze book pricing trends and distribution using scraped data.

Use the filters to explore insights.
""")

# ======================
# LOAD DATA
# ======================
df = pd.read_csv("data.csv")

# ======================
# SIDEBAR FILTERS
# ======================
st.sidebar.header("🔍 Filters")

min_price, max_price = st.sidebar.slider(
    "Price Range",
    float(df["Price"].min()),
    float(df["Price"].max()),
    (10.0, 50.0)
)

# ======================
# APPLY FILTER
# ======================
filtered = df[
    (df["Price"] >= min_price) &
    (df["Price"] <= max_price)
]

# ======================
# METRICS
# ======================
col1, col2 = st.columns(2)

col1.metric("Total Books", len(filtered))
col2.metric("Average Price", round(filtered["Price"].mean(), 2))

# ======================
# DATA TABLE
# ======================
st.subheader("📄 Product Data")
st.dataframe(filtered)

# ======================
# HISTOGRAM (BETTER THAN BAR)
# ======================
st.subheader("💰 Price Distribution")

fig, ax = plt.subplots()
filtered["Price"].hist(bins=20, ax=ax)
st.pyplot(fig)

st.markdown("""
**Insight:** Most books are priced within a mid-range band.

**Business Impact:** Pricing consistency suggests standardized market positioning.
""")

# ======================
# LAST UPDATED
# ======================
st.caption(f"🕒 Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")