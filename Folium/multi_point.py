import folium
import pandas
data = pandas.read_csv("Folium/Volcanoes.txt")
lon = list(data["LON"])
lat = list(data["LAT"])

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles ="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

for lt, ln in zip(lat, lon):
    fg.add_child(folium.Marker(location=[lt, ln], popup="Hi, I Am Marker", icon=folium.Icon(color='blue')))

map.add_child(fg)
map.save("Folium/Map3.html")