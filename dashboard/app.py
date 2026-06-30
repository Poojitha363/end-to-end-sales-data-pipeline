import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

# Page Configuration
st.set_page_config(page_title="Sales Dashboard", layout="wide")

st.title("📊 Sales Dashboard")

# Database Connection
db_url = URL.create(
    drivername="postgresql+psycopg2",
    username="postgres",
    password="Poojitha@789",
    host="localhost",
    port="5432",
    database="end_to_end_pipeline",
)

engine = create_engine(db_url)

# Load Data
query = "SELECT * FROM clean_sales"
df = pd.read_sql(query, engine)

# ---------------- Sidebar Filter ----------------

# Convert order_date to datetime
df["order_date"] = pd.to_datetime(df["order_date"])

# Sidebar Filters
st.sidebar.header("Filters")

# Date Filter
min_date = df["order_date"].min().date()
max_date = df["order_date"].max().date()

selected_dates = st.sidebar.date_input(
    "Select Date Range",
    [min_date, max_date]
)

# City Filter
selected_city = st.sidebar.selectbox(
    "Select City",
    ["All"] + sorted(df["city"].unique().tolist())
)

# Product Filter
selected_product = st.sidebar.selectbox(
    "Select Product",
    ["All"] + sorted(df["product"].unique().tolist())
)

# Category Filter
selected_category = st.sidebar.selectbox(
    "Select Category",
    ["All"] + sorted(df["category"].unique().tolist())
)

# Apply Filters
if len(selected_dates) == 2:
    start_date, end_date = selected_dates
    df = df[
        (df["order_date"].dt.date >= start_date)
        & (df["order_date"].dt.date <= end_date)
    ]

if selected_city != "All":
    df = df[df["city"] == selected_city]

if selected_product != "All":
    df = df[df["product"] == selected_product]

if selected_category != "All":
    df = df[df["category"] == selected_category]

# ---------------- KPI Cards ----------------

col1, col2, col3 = st.columns(3)

col1.metric("Total Orders", len(df))
col2.metric("Total Sales", f"₹ {df['total_amount'].sum():,.2f}")
col3.metric("Average Sales", f"₹ {df['total_amount'].mean():,.2f}")

st.divider()

# ---------------- City-wise Sales ----------------

st.subheader("🏙️ City-wise Sales")

city_sales = (
    df.groupby("city")["total_amount"]
    .sum()
    .reset_index()
)

fig1 = px.bar(
    city_sales,
    x="city",
    y="total_amount",
    title="City-wise Sales"
)

st.plotly_chart(fig1, use_container_width=True)

# ---------------- Top Products ----------------

st.subheader("📦 Top Products")

top_products = (
    df.groupby("product")["quantity"]
    .sum()
    .reset_index()
    .sort_values(by="quantity", ascending=False)
    .head(10)
)

fig2 = px.bar(
    top_products,
    x="product",
    y="quantity",
    title="Top 10 Products"
)

st.plotly_chart(fig2, use_container_width=True)


# ---------------- Pie Chart ----------------

st.subheader("Sales by Category")

pie = px.pie(
    df,
    names="category",
    values="total_amount",
    title="Sales by Category"
)

st.plotly_chart(pie, use_container_width=True)


# ---------------- Line Chart ----------------
st.subheader("Daily Sales Trend")

daily_sales = (
    df.groupby("order_date")["total_amount"]
    .sum()
    .reset_index()
)

fig3 = px.line(
    daily_sales,
    x="order_date",
    y="total_amount",
    title="Daily Sales Trend"
)

st.plotly_chart(fig3, use_container_width=True)

# ---------------- Download CSV button ----------------

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="📥 Download Filtered Data",
    data=csv,
    file_name="filtered_sales.csv",
    mime="text/csv"
)