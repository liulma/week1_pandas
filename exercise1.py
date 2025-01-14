import pandas as pd

# Exercise 1.1: Create dataframe
data = {
    'Name': ['Teresa', 'Maria', 'John', 'Peter', 'Tom'],
    'Age': [30, 48, 30, 33, 24],
    'Score': [5, 8, 4, 9, 7]
}

df = pd.DataFrame(data)

print("Original dataframe:")
print(df)

# Exercise 1.2: Set the 'Name' column as the index and slice the DataFrame to display information about individuals over the age of 25
df_indexed = df.set_index('Name')

filtered_df = df_indexed[df_indexed['Age'] > 25]

print("Filtered to show only people who are over 25 years old:")
print(filtered_df)
print()

# Exercise 1.3: Convert data type of 'Score' column to float
df['Score'] = df['Score'].astype(float)

# Exercise 1.4: Grouping data by 'Age' and calculate mean score for each age group
grouped_df = df.groupby('Age').mean('Score')

print("Grouped by age, mean of scores:")
print(grouped_df)