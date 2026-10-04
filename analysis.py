import pandas as pd

# Load the data
df = pd.read_csv('sales_data.csv')

print("--- Sales Data Analytics Project ---\n")
print("First 5 rows:")
print(df.head())

print("\nTotal Sales:", df['Sales'].sum())
print("\nSales by Product:")
print(df.groupby('Product')['Sales'].sum())

print("\nSales by Region:")
print(df.groupby('Region')['Sales'].sum())

print("\n--- Key Insight ---")
top_product = df.groupby('Product')['Sales'].sum().idxmax()
print(f"Top selling product is: {top_product}")
