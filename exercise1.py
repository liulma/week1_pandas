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