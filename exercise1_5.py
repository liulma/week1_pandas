import pandas as pd

# Exercise 1.5: Introduce some missing values in 'Score' and fill missing values
data = {
    'Name': ['Teresa', 'Maria', 'John', 'Peter', 'Tom'],
    'Age': [30, 48, 30, 33, 24],
    'Score': [5, None, 4, None, 7]
}

df = pd.DataFrame(data)

df_filled = df.fillna({'Score': df['Score'].mean().round(2)})

print("None -values filled with the mean score:")
print(df_filled)