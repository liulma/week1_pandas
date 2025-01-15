import pandas as pd

# Exercise 2.4: New dataset which displays the average fare per sex and Pclass
file_path = 'titanic.csv'

df = pd.read_csv(file_path)

grouped_df = df.groupby(['Sex', 'Pclass'])['Fare'].mean().reset_index()

print(grouped_df)