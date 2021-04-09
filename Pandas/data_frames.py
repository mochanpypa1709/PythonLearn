import pandas
df1 = pandas.DataFrame([[2,4,6],[10,20,30]])
df2 = pandas.DataFrame([[2,4,6],[10,20,30]], columns = ["Price","Age","Value"], index = ["First","Second"])
df3 = pandas.DataFrame([{"Name":"John","Surname":"Ji"},{"Name":"Jack"}])
print(df3)

