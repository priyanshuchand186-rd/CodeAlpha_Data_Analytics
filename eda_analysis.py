import pandas as pd
from pathlib import Path

# Get current Python file location
BASE_DIR = Path(__file__).resolve().parent

# Dataset file path
file_path = BASE_DIR / "Sample - Superstore.csv"

# Load dataset
df = pd.read_csv(file_path, encoding="latin1")

# Display first 5 rows
print("\nFirst 5 Rows:")
print(df.head())

# Display dataset shape
print("\nDataset Shape:", df.shape)

print("\nDataset loaded successfully!")
# 1. Dataset Information
print("\n--- DATASET INFORMATION ---")
df.info()

# 2. Column Names
print("\n--- COLUMN NAMES ---")
print(df.columns.tolist())

# 3. Statistical Summary
print("\n--- STATISTICAL SUMMARY ---")
print(df.describe())

# 4. Dataset Shape
print("\n--- DATASET SHAPE ---")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# 5. Check Missing Values

print("\n--- MISSING VALUES ---")

missing_values = df.isnull().sum()

print(missing_values)

print("\nTotal Missing Values:")
print(missing_values.sum())


# 6. Check Duplicate Records

print("\n--- DUPLICATE RECORDS ---")

duplicates = df.duplicated().sum()

print("Total Duplicate Rows:", duplicates)

# STEP 5: DATA CLEANING

print("\n--- DATA CLEANING ---")

# Convert dates into datetime format

df['Order Date'] = pd.to_datetime(
    df['Order Date'],
    format='%m/%d/%Y'
)

df['Ship Date'] = pd.to_datetime(
    df['Ship Date'],
    format='%m/%d/%Y'
)

# Check updated data types

print("\nUpdated Data Types:")
print(df[['Order Date', 'Ship Date']].dtypes)

# Check date range

print("\nOrder Date Range:")
print("First Order:", df['Order Date'].min())
print("Last Order:", df['Order Date'].max())

print("\nData Cleaning Completed Successfully!")

# STEP 6: CATEGORY-WISE SALES ANALYSIS

print("\n--- CATEGORY-WISE SALES ---")

category_sales = df.groupby('Category')['Sales'].sum()

print(category_sales)

print("\nCategory with Highest Sales:")
print(category_sales.idxmax())

print("\nHighest Sales Amount:")
print(category_sales.max())

# STEP 7: REGION-WISE PROFIT ANALYSIS

print("\n--- REGION-WISE PROFIT ---")

region_profit = df.groupby('Region')['Profit'].sum()

print(region_profit)

print("\nRegion with Highest Profit:")
print(region_profit.idxmax())

print("\nHighest Profit Amount:")
print(region_profit.max())

# STEP 8: CATEGORY-WISE PROFIT ANALYSIS

print("\n--- CATEGORY-WISE PROFIT ---")

category_profit = df.groupby('Category')['Profit'].sum()

print(category_profit)

print("\nCategory with Lowest Profit:")
print(category_profit.idxmin())

print("\nLowest Profit Amount:")
print(category_profit.min())

# STEP 9: MONTHLY SALES TREND

print("\n--- MONTHLY SALES TREND ---")

df['Year-Month'] = df['Order Date'].dt.to_period('M')

monthly_sales = df.groupby('Year-Month')['Sales'].sum()

print(monthly_sales)

print("\nMonth with Highest Sales:")
print(monthly_sales.idxmax())

print("\nHighest Monthly Sales:")
print(monthly_sales.max())

