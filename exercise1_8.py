import pandas as pd

#Exercise 1.8: Dataframe with datetime
data = {
    'Date': ['1994-02-23', '1990-01-24', '2023-09-23', '2015-03-07', '2022-05-27'],
    'Value': [1, 2, 4, 8, 9]
}

df = pd.DataFrame(data)

df['Date'] = pd.to_datetime(df['Date'])

print("Datetime:")
print(df)