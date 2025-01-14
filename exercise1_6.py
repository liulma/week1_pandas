import pandas as pd

# Exercise 1.6: Create another DataFrame and concatete it with the previous one
data = {
    'Name': ['Teresa', 'Maria', 'John', 'Peter', 'Tom'],
    'Age': [30, 48, 30, 33, 24],
    'Score': [5, 8, 4, 9, 7]
}

data2 = {
    'Name': ['Michael', 'James', 'Jenny', 'Matthew', 'Alisa'],
    'Age': [22, 50, 41, 31, 31],
    'Occupation': ['Software Engineer', 'Cashier', 'Data Engineer', 'Construction worker', 'System specialist']
}

df = pd.DataFrame(data)
df2 = pd.DataFrame(data2)

print("New dataframe:")
print(df2)
print()

concatenated_df = pd.concat([df, df2], ignore_index=True)

print("Concatenated dataframe:")
print(concatenated_df)