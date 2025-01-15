import pandas as pd

# Exercise 2.3: Set sex to be child for all persons under the age of 18
file_path = 'titanic.csv'

df = pd.read_csv(file_path)

df.loc[df['Age'] < 18, 'Sex'] = 'child'

print(df)