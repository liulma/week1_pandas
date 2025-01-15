import pandas as pd

# Exercise 2.6: New dataset which displays the average fare per survived
file_path = 'titanic.csv'

df = pd.read_csv(file_path)

grouped_df = df.groupby('Survived')['Fare'].mean().reset_index()

print(grouped_df)