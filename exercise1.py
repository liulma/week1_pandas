import pandas as pd

# Create dataframe
data = {
    'Name': ['Teresa', 'Maria', 'John', 'Peter', 'Tom'],
    'Age': [30, 48, 22, 33, 24],
    'Score': [5, 8, 4, 9, 7]
}

df = pd.DataFrame(data)

df_indexed = df.set_index('Name')

filtered_df = df_indexed[df_indexed['Age'] > 25]

print(filtered_df)