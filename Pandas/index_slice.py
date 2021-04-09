import pandas
df2=pandas.read_json("Pandas/supermarkets.json")
df2=df2.set_index("Address")
locate = df2.loc["332 Hill St","Country"]
slicing = df2.iloc[3,1:4]
drop = df2.drop("332 Hill St")
print(df2)
print(locate)
print(slicing)
print(drop)