#install folium
#type --> pip3.9 install folium

import folium
map = folium.Map(location=[-6.80, 108], zoom_start=8, tiles ="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

for coordinate in [[-6.56, 106.78],[-6.40, 105.78]]:
    fg.add_child(folium.Marker(location=coordinate, popup="Hi, I Am Marker", icon=folium.Icon(color='blue')))

map.add_child(fg)
map.save("Folium/Map2.html")
