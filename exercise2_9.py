import pandas as pd

# Exercise 9: Filter off persons who had both siblings/spouces AND parents children
file_path = 'titanic.csv'

df = pd.read_csv(file_path)

filtered_df = df[(df['Siblings/Spouses Aboard'] > 0) & (df['Parents/Children Aboard'] > 0)]

print(filtered_df)