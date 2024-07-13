# ETL Data Analytics with Python

## Overview

This project demonstrates a simple ETL (Extract, Transform, Load) pipeline using Python and the `pandas` library. The ETL process involves extracting data from CSV files, transforming it by merging and filtering, and then loading the transformed data into a new CSV file. This project uses sample sales and product datasets to illustrate the process.

## Data Sets

### `sales.csv`
Contains sales data:
```csv
order_id,product_id,quantity,price,date
1,101,2,9.99,2023-01-01
2,103,1,19.99,2023-01-03
3,104,5,4.99,2023-01-04
4,101,3,9.99,2023-01-05
5,102,2,14.99,2023-01-07
```

### `products.csv`
Contains product information:
```csv
product_id,product_name,category
101,Widget A,Gadgets
102,Widget B,Gadgets
103,Thingamajig,Widgets
104,Doodad,Widgets
```

## ETL Process

The ETL process involves the following steps:

1. **Extract**: Load data from CSV files.
2. **Transform**: 
   - Merge sales data with product data.
   - Add a new column for the total sales amount.
   - Filter data to include only sales of products in the "Gadgets" category.
3. **Load**: Save the transformed data to a new CSV file.

## Dependencies

- Python 3.x
- `pandas` library

## Installation

1. Install Python 3.x from [python.org](https://www.python.org/).
2. Install the `pandas` library using pip:
   ```bash
   pip install pandas
   ```

## Running the ETL Script

1. Place the `sales.csv` and `products.csv` files in your working directory.
2. Create a Python script file, e.g., `etl.py`, and paste the following code into it:

   ```python
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
   ```

3. Run the script:
   ```bash
   python etl.py
   ```

4. After running the script, you will find a new file `gadgets_sales.csv` in your working directory containing the transformed data.

## Transformed Data Sample (`gadgets_sales.csv`)

The output file will contain data filtered to only include sales of products in the "Gadgets" category, along with a new column for the total sales amount:
```csv
order_id,product_id,quantity,price,date,product_name,category,total_sales
1,101,2,9.99,2023-01-01,Widget A,Gadgets,19.98
4,101,3,9.99,2023-01-05,Widget A,Gadgets,29.97
5,102,2,14.99,2023-01-07,Widget B,Gadgets,29.98
```

## License

This project is licensed under the Apache License.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Contact

For any questions or suggestions, please open an issue or contact me directly.
