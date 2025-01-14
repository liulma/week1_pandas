import pandas as pd

#Exercise 1.9: Rename columns in DataFrame to EventDate and EventValue for another randomly chosen column
data = {
    'Date': ['1994-02-23', '1990-01-24', '2023-09-23', '2015-03-07', '2022-05-27'],
    'Value': [1, 2, 4, 8, 9]
}

df = pd.DataFrame(data)

df_renamed = df.rename(columns={'Date': 'EventDate', 'Value': 'EventValue'})

print("Renamed columns:")
print(df_renamed)