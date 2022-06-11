import pandas as pd


df = pd.read_json('Employees.json')

print(df.to_string())

print(df.dtypes)