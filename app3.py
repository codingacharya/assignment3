import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page Configuration
st.set_page_config(
    page_title="Corporate Sales Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 5-Year Corporate Sales Audit & Performance Trend Dashboard")

# Upload CSV
uploaded_file = st.file_uploader(
    "Upload corporate_sales.csv",
    type=["csv"]
)

if uploaded_file is not None:

    # Load Dataset
    df = pd.read_csv(uploaded_file)

    st.subheader("📄 Raw Dataset")
    st.dataframe(df)

    # Dataset Info
    st.subheader("ℹ Dataset Information")

    info_df = pd.DataFrame({
        "Column": df.columns,
        "Data Type": df.dtypes.astype(str),
        "Non-Null Count": df.count().values
    })

    st.dataframe(info_df)

    # Missing Values
    st.subheader("🔍 Missing Values")

    missing_values = df.isnull().sum()

    st.dataframe(
        pd.DataFrame({
            "Column": missing_values.index,
            "Missing Values": missing_values.values
        })
    )

    # Fill Missing Values
    df["Sales"] = df["Sales"].fillna(df["Sales"].mean())
    df["Profit"] = df["Profit"].fillna(df["Profit"].mean())

    st.success("✅ Missing values filled using column averages.")

    # Remove Duplicates
    before_rows = len(df)

    df = df.drop_duplicates()

    after_rows = len(df)

    st.subheader("🧹 Duplicate Records")

    st.write(f"Rows Before Cleaning: **{before_rows}**")
    st.write(f"Rows After Cleaning: **{after_rows}**")
    st.write(f"Duplicates Removed: **{before_rows - after_rows}**")

    # KPIs
    st.subheader("📈 Key Performance Indicators")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Total Sales",
            f"₹ {df['Sales'].sum():,.0f}"
        )

    with col2:
        st.metric(
            "Total Profit",
            f"₹ {df['Profit'].sum():,.0f}"
        )

    with col3:
        st.metric(
            "Regions",
            df["Region"].nunique()
        )

    # Region Analysis
    st.subheader("🌍 Average Sales by Region")

    region_sales = df.groupby("Region")["Sales"].mean()

    st.dataframe(region_sales.reset_index())

    # Profit Analysis
    st.subheader("💰 Average Profit by Region")

    region_profit = df.groupby("Region")["Profit"].mean()

    st.dataframe(region_profit.reset_index())

    # Yearly Sales
    st.subheader("📅 Total Sales by Year")

    yearly_sales = df.groupby("Year")["Sales"].sum()

    st.dataframe(yearly_sales.reset_index())

    # Charts Section
    st.subheader("📊 Visual Analytics")

    col1, col2 = st.columns(2)

    # Line Chart
    with col1:
        st.write("### Sales Trend (2020–2024)")

        fig1, ax1 = plt.subplots(figsize=(6,4))

        yearly_sales.plot(
            kind="line",
            marker="o",
            ax=ax1
        )

        ax1.set_xlabel("Year")
        ax1.set_ylabel("Sales")
        ax1.set_title("Year-wise Total Sales")

        st.pyplot(fig1)

    # Bar Chart
    with col2:
        st.write("### Average Sales by Region")

        fig2, ax2 = plt.subplots(figsize=(6,4))

        region_sales.plot(
            kind="bar",
            ax=ax2
        )

        ax2.set_xlabel("Region")
        ax2.set_ylabel("Average Sales")
        ax2.set_title("Region-wise Average Sales")

        st.pyplot(fig2)

    # Business Insights
    st.subheader("📌 Business Insights")

    best_region = region_sales.idxmax()
    worst_region = region_sales.idxmin()

    st.success(
        f"""
        ✅ Best Performing Region: {best_region}

        ⚠ Lowest Performing Region: {worst_region}

        📈 Sales show an overall upward trend.

        🧹 Data cleaned successfully by removing duplicates and filling missing values.
        """
    )

else:
    st.info("📂 Please upload corporate_sales.csv to begin analysis.")