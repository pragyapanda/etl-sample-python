import pandas as pd

# Step 1: Extract
# Load data from CSV files
sales_df = pd.read_csv('sales.csv')
products_df = pd.read_csv('products.csv')

# Step 2: Transform
# Merge sales data with product data to get product details in sales records
merged_df = pd.merge(sales_df, products_df, on='product_id', how='left')

# Add a new column for total sales amount
merged_df['total_sales'] = merged_df['quantity'] * merged_df['price']

# Filter data to only include sales of Gadgets category
gadgets_sales_df = merged_df[merged_df['category'] == 'Gadgets']

# Step 3: Load
# Save the transformed data to a new CSV file
gadgets_sales_df.to_csv('gadgets_sales.csv', index=False)

# Display the transformed data
print(gadgets_sales_df)
