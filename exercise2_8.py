import pandas as pd

# Exercise 2.8: New dataset with Pclass, Name and Age, for persons who have siblings, spouses, parents or children abroad
file_path = 'titanic.csv'

df = pd.read_csv(file_path)

mask = (df['Siblings/Spouses Aboard'] > 0) | (df['Parents/Children Aboard'] > 0)
new_df = df.loc[mask, ['Pclass', 'Name', 'Age']]

print(new_df)