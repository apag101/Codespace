import matplotlib.pyplot as plt
import pandas as pd

# Assuming CSV file format
file_path = 'sales_by_region.csv'
# Read data from CSV
sales_df = pd.read_csv(file_path)

# Creating the bar chart
plt.figure(figsize=(10, 6))
plt.bar(sales_df['Region'], sales_df['Sales'], color='blue')
plt.title('Sales by Region')
plt.xlabel('Region')
plt.ylabel('Sales')
plt.grid(axis='y')

# Saving the plot to a file
plt.savefig('sales_by_region.png')
plt.show()