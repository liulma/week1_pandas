import pandas as pd

# Exercise 1.7: Create two DataFrames and merge them based on ID
data3 = {
    'ID': [1, 2, 3, 4, 5],
    'Name': ['Elsa', 'Mathilda', 'Miranda', 'Jack', 'Tim'],
    'Age': [30, 45, 60, 30, 24]
}

data4 = {
    'ID': [1, 2, 3, 4, 5],
    'Occupation': ['Project Engineer', 'Service Coordinator', 'Cashier', 'Nurse', 'Janitor'],
    'Salary': [3500, 4500, 2800, 3300, 2400]
}

df3 = pd.DataFrame(data3)
df4 = pd.DataFrame(data4)

merged_df = pd.merge(df3, df4, on='ID', how='inner')

print("Merged dataframe:")
print(merged_df)