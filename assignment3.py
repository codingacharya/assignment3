import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("corporate_sales.csv")

# Display first 5 records
print("First 5 Records:")
print(df.head())

# Dataset information
print("\nDataset Information:")
print(df.info())

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing values with mean
df["Sales"] = df["Sales"].fillna(df["Sales"].mean())
df["Profit"] = df["Profit"].fillna(df["Profit"].mean())

# Remove duplicate rows
df = df.drop_duplicates()

# Average Sales by Region
region_sales = df.groupby("Region")["Sales"].mean()
print("\nAverage Sales by Region:")
print(region_sales)

# Average Profit by Region
region_profit = df.groupby("Region")["Profit"].mean()
print("\nAverage Profit by Region:")
print(region_profit)

# Total Sales by Year
yearly_sales = df.groupby("Year")["Sales"].sum()
print("\nTotal Sales by Year:")
print(yearly_sales)

# Line Chart
yearly_sales.plot(
    kind="line",
    marker="o",
    title="Year-wise Total Sales Trend"
)
plt.xlabel("Year")
plt.ylabel("Total Sales")
plt.grid(True)
plt.show()

# Bar Chart
region_sales.plot(
    kind="bar",
    title="Average Sales by Region"
)
plt.xlabel("Region")
plt.ylabel("Average Sales")
plt.show()