import pandas as pd

#Exercise 1.10: Create DataFrame with a column containing repetitive values, display the unique values in that column
data = {
    'ID': [1, 2, 3, 4, 5],
    'Name': ['Elsa', 'Mathilda', 'Mathilda', 'Jack', 'Jack'],
    'Age': [30, 45, 60, 30, 24]
}

df = pd.DataFrame(data)

unique_names = df['Name'].unique()

print("Unique values:")
print(unique_names)