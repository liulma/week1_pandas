import pandas as pd

# Exercise 2.2: Rename columns not to have any whitespace or special characters
file_path = 'titanic.csv'

df = pd.read_csv(file_path)

df = df.rename(columns=lambda x: x.replace(' ', '_').replace('/', '_'))

print(df)