import pandas
df1=pandas.read_csv("Pandas/supermarkets.csv")
df2=pandas.read_json("Pandas/supermarkets.json")
df3=pandas.read_excel("Pandas/supermarkets.xlsx",sheet_name=0)
df4=pandas.read_csv("Pandas/supermarkets-commas.txt")
df5=pandas.read_csv("Pandas/supermarkets-semi-colons.txt",sep=';')

#add header
df6=pandas.read_csv("Pandas/no_header.txt")
df6.columns = ("ID","Address","City","Zip","Country","Name","Employee")

#geocode
from geopy.geocoders import ArcGIS
nom = ArcGIS()
df1["Address"]=df1["Address"]+", "+df1["City"]+", "+df1["State"]+", "+df1["Country"]
df1["Coordinates"]=df1["Address"].apply(nom.geocode)
df1["Latitude"]=df1["Coordinates"].apply(lambda x: x.latitude if x !=None else None) 
print(df1)