import folium
import pandas

data=pandas.read_csv("Volcanoes.txt")
lat=list(data['LAT'])
lon=list(data['LON'])

map=folium.Map(location=[56.344562, 37.524296],zoom_start=6,tiles = "Stamen Terrain")

fg=folium.FeatureGroup(name="Volcanoes")
for coord in zip(lat,lon):
    fg.add_child(folium.Marker(location=coord,popup="HIIII!",icon=folium.Icon(color='green'))) #add marker

map.add_child(fg)

map.save("1.html") # create html file with map

