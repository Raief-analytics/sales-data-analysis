import pandas as pd

# Load the sales data
df = pd.read_csv("sales.csv")

# Calculate total sales
print("Total Sales:", df["Sales"].sum())
