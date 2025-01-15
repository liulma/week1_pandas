import pandas as pd

# Exercise 10: Average pay of persons who had both siblings/spouces AND parents children
file_path = 'titanic.csv'

df = pd.read_csv(file_path)

filtered_df = df[(df['Siblings/Spouses Aboard'] > 0) & (df['Parents/Children Aboard'] > 0)]

average_fare = filtered_df['Fare'].mean()

print("Filtered dataframe:")
print(filtered_df)
print()
print(f"Average fare: {average_fare}")