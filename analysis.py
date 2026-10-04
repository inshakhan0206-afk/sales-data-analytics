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
import matplotlib.pyplot as plt
#sales by product 
product_sales = df.groupby('Product')['Sales'].sum()

plt.figure(figsize=(8,5))
product_sales.plot(kind='bar')
plt.title('Sales by Product')
plt.xlabel('Product')
plt.ylabel('Sales')
plt.tight_layout()
plt.savefig('charts/sales_by_product.png')
plt.show()
#sales by region
region_sales = df.groupby('Region')['Sales'].sum()
plt.figure(figsize=(8,5))
region_sales.plot(kind='bar')
plt.title('Sales by Region')
plt.xlabel('Region')
plt.ylabel('Sales')
plt.tight_layout()
plt.savefig('charts/sales_by_region.png')
plt.show()
#sales by month
month_order = ['Jan', 'Feb', 'Mar']

df['Month'] = pd.Categorical(
    df['Month'],
    categories=month_order,
    ordered=True
)

monthly_sales = df.groupby('Month', observed=True)['Sales'].sum()
plt.figure(figsize=(8,5))
monthly_sales.plot(kind='line', marker='o')
plt.title('Sales by Month')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.tight_layout()
plt.savefig('charts/sales_by_month.png')
plt.show()
