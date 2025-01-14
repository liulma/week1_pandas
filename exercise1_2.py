# Exercise 1.2: Set the 'Name' column as the index and slice the DataFrame to display information about individuals over the age of 25
import pandas as pd

data = {
    'Name': ['Teresa', 'Maria', 'John', 'Peter', 'Tom'],
    'Age': [30, 48, 30, 33, 24],
    'Score': [5, 8, 4, 9, 7]
}

df = pd.DataFrame(data)
df_indexed = df.set_index('Name')

filtered_df = df_indexed[df_indexed['Age'] > 25]

print("Filtered to show only people who are over 25 years old:")
print(filtered_df)