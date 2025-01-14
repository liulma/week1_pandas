import pandas as pd

# Exercise 1.1: Create dataframe
data = {
    'Name': ['Teresa', 'Maria', 'John', 'Peter', 'Tom'],
    'Age': [30, 48, 30, 33, 24],
    'Score': [5, 8, 4, 9, 7]
}

df = pd.DataFrame(data)

# Exercise 1.2: Set the 'Name' column as the index and slice the DataFrame to display information about individuals over the age of 25
df_indexed = df.set_index('Name')

filtered_df = df_indexed[df_indexed['Age'] > 25]

print(filtered_df)

# Exercise 1.3: Convert data type of 'Score' column to float
df['Score'] = df['Score'].astype(float)
