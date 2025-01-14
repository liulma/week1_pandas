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
print()

# Exercise 1.5: Introduce some missing values in 'Score' and fill missing values
df.replace({'Score': {8.0: None , 9.0: None}}, inplace=True)

df_filled = df.fillna({'Score': df['Score'].mean().round(2)})

print("None -values filled with the mean score:")
print(df_filled)
print()

# Exercise 1.6: Create another DataFrame and concatete it with the previous one
data2 = {
    'Name': ['Michael', 'James', 'Jenny', 'Matthew', 'Alisa'],
    'Age': [22, 50, 41, 31, 31],
    'Occupation': ['Software Engineer', 'Cashier', 'Data Engineer', 'Construction worker', 'System specialist']
}

df2 = pd.DataFrame(data2)

print("New dataframe:")
print(df2)
print()

concatenated_df = pd.concat([df, df2], ignore_index=True)

print("Concatenated dataframe:")
print(concatenated_df)