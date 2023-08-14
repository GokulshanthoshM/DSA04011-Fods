import pandas as pd

# Sample data (replace this with your actual data loading code)
data = {
    'Product': ['Product A', 'Product B', 'Product A', 'Product C', 'Product B'],
    'Quantity Sold': [10, 5, 8, 12, 6],
    'Date': ['2023-07-05', '2023-07-10', '2023-07-15', '2023-07-20', '2023-07-25']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Convert 'Date' column to datetime type
df['Date'] = pd.to_datetime(df['Date'])

# Filter data for the past month
past_month = df[df['Date'] >= df['Date'].max() - pd.DateOffset(months=1)]

# Group and summarize data
product_summary = past_month.groupby('Product')['Quantity Sold'].sum()

# Sort data in descending order and get top 5 products
top_products = product_summary.sort_values(ascending=False).head(5)

print(top_products)
