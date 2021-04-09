import pandas
df1=pandas.read_csv("Pandas/supermarkets.csv")
df2=pandas.read_json("Pandas/supermarkets.json")
df3=pandas.read_excel("Pandas/supermarkets.xlsx",sheet_name=0)
df4=pandas.read_csv("Pandas/supermarkets-commas.txt")
df5=pandas.read_csv("Pandas/supermarkets-semi-colons.txt",sep=';')
print(df5)