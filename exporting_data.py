
import pandas as pd
import os

data = {
    'product': ['Laptop', 'Tablet', 'Smartphone', 'Desktop'],
    'price': [1000, 500, 800, 1200]
}

df = pd.DataFrame(data)

# Save the CSV file in the current folder
df.to_csv('products.csv', index=False, header=True)

print("CSV file exported successfully!")
print(df)

print("File location:", os.path.abspath('products.csv'))



import pandas as pd
import os

data = {
    'product': ['Laptop', 'Tablet', 'Smartphone', 'Desktop'],
    'price': [1000, 500, 800, 1200],
    'quantity': [5, 10, 15, 3]
}

df = pd.DataFrame(data)

# Create an output folder
os.makedirs("exports", exist_ok=True)

# 1. Export to CSV
df.to_csv("exports/products.csv", index=False)

# 2. Export to Excel
df.to_excel("exports/products.xlsx", index=False)

# 3. Export to JSON
df.to_json("exports/products.json", orient="records", indent=4)

print("All files exported successfully!")
print(df)

