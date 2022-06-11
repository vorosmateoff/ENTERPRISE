import pandas as pd


df = pd.read_xml('Employees.xml')
print(df)
print(df.dtypes)

df['Childrens'].dtypes