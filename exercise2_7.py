import pandas as pd

# Exercise 2.7: Split dataset into 3 datasets per sex
file_path = 'titanic.csv'

df = pd.read_csv(file_path)

male_df = df[df['Sex'] == 'male'].reset_index()
female_df = df[df['Sex'] == 'female'].reset_index()
child_df = df[df['Sex'] == 'child'].reset_index()

print(male_df)
print()
print(female_df)
print()
print(child_df)