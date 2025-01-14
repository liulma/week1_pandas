import pandas as pd

# Exercise 1.4: Grouping data by 'Age' and calculate mean score for each age group
data = {
    'Name': ['Teresa', 'Maria', 'John', 'Peter', 'Tom'],
    'Age': [30, 48, 30, 33, 24],
    'Score': [5, 8, 4, 9, 7]
}

df = pd.DataFrame(data)

grouped_df = df.groupby('Age').mean('Score')

print("Grouped by age, mean of scores:")
print(grouped_df)