import pandas as pd
import matplotlib.pyplot as plt

# Reading monthly sales data from CSV

df = pd.read_csv('monthly_sales.csv')

# Plotting the data
plt.figure(figsize=(10, 6))
plt.bar(df['Month'], df['Sales'], color='skyblue')
plt.title('Monthly Sales Data')
plt.xlabel('Month')
plt.ylabel('Sales ($)')
plt.xticks(rotation=45)
plt.tight_layout()

# Saving the plot as a PNG file
plt.savefig('monthly_sales.png')
plt.show()