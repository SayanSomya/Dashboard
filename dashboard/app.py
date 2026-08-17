import streamlit as st
import pandas as pd
import plotly.express as px
from utils.insights import generate_insight

st.set_page_config(
    page_title="Filtered Sales Dashboard",
    layout="wide"
)

st.title("📊 Filtered Sales Dashboard")

try:
    # Load data
    df = pd.read_csv("data\sales_data.csv")
    st.success("✅ CSV loaded successfully")

    # Region filter
    st.sidebar.header("Filter Options")

    region = st.sidebar.selectbox(
        "Choose Region",
        df["region"].unique()
    )

    # Filter data
    filtered_df = df[df["region"] == region]

    # Show filtered table
    st.subheader(f"Sales Data for Region: {region}")
    st.dataframe(filtered_df)

    # Bar chart
    st.subheader("📦 Total Sales by Product")

    fig = px.bar(
        filtered_df,
        x="product",
        y="total_sales",
        color="status",
        title=f"Sales Breakdown by Product in {region}"
    )

    st.plotly_chart(fig, use_container_width=True)

    # AI Insight
    st.subheader("🔍 AI Insight")
    st.info(generate_insight(filtered_df))

except Exception as e:
    st.error(f"❌ Something went wrong: {e}")
