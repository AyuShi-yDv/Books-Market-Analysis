import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# ==============================
# PAGE CONFIG
# ==============================
st.set_page_config(page_title="Books Market Analysis", layout="wide")

# ==============================
# HEADER
# ==============================
st.title("📚 Books Market Analysis Dashboard")

st.markdown("""
### 🎯 Objective  
Analyze pricing and rating trends of books using scraped data.

### 📊 Key Capabilities:
- Explore price distribution  
- Analyze rating patterns  
- Identify high-quality books  
- Understand price vs rating relationship  
""")

# ==============================
# LOAD DATA
# ==============================
df = pd.read_csv("data.csv")

# ==============================
# SIDEBAR FILTERS
# ==============================
st.sidebar.header("🔍 Filters")

min_price, max_price = st.sidebar.slider(
    "💰 Price Range",
    float(df["Price"].min()),
    float(df["Price"].max()),
    (10.0, 50.0)
)

rating = st.sidebar.slider("⭐ Minimum Rating", 1, 5, 3)

# ==============================
# APPLY FILTERS
# ==============================
filtered = df[
    (df["Price"] >= min_price) &
    (df["Price"] <= max_price) &
    (df["Rating"] >= rating)
]

# ==============================
# METRICS
# ==============================
st.subheader("📌 Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("📚 Total Books", len(filtered))
col2.metric("💰 Avg Price", round(filtered["Price"].mean(), 2))
col3.metric("⭐ Avg Rating", round(filtered["Rating"].mean(), 2))

# ==============================
# DATA TABLE
# ==============================
st.subheader("📄 Filtered Data")
st.dataframe(filtered)

# ==============================
# PRICE DISTRIBUTION
# ==============================
st.subheader("💰 Price Distribution")

fig1, ax1 = plt.subplots()
filtered["Price"].hist(bins=20, ax=ax1)
st.pyplot(fig1)

st.markdown("""
**Insight:** Most books fall within a mid-price range.

**Business Impact:** Standardized pricing suggests competitive market positioning.
""")

# ==============================
# RATING DISTRIBUTION
# ==============================
st.subheader("⭐ Rating Distribution")

st.bar_chart(filtered["Rating"].value_counts())

st.markdown("""
**Insight:** Majority of books have above-average ratings.

**Business Impact:** Higher-rated books tend to attract more user trust.
""")

# ==============================
# PRICE VS RATING (KEY ANALYSIS)
# ==============================
st.subheader("📈 Price vs Rating")

st.scatter_chart(filtered[["Price", "Rating"]])

st.markdown("""
**Insight:** Price does not strongly correlate with rating.

**Business Impact:** Higher pricing does not guarantee better product perception.
""")

# ==============================
# UPDATED
# ==============================
st.caption(f"🕒 Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# ==============================
# FOOTER
# ==============================
st.markdown("---")
st.markdown("🚀 Built with Streamlit | End-to-End Data Analysis Project")