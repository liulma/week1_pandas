import pandas as pd

# Exercise 1.3: Convert data type of 'Score' column to float
data = {
    'Name': ['Teresa', 'Maria', 'John', 'Peter', 'Tom'],
    'Age': [30, 48, 30, 33, 24],
    'Score': [5, 8, 4, 9, 7]
}

df = pd.DataFrame(data)

df['Score'] = df['Score'].astype(float)

print(df)