import folium
import pandas

data=pandas.read_csv("Volcanoes.txt")
lat=list(data['LAT'])
lon=list(data['LON'])
elev=list(data['ELEV'])
name = list(data["NAME"])

map=folium.Map(location=[38, -99],zoom_start=6,tiles = "Stamen Terrain")

html1 = """<h4>Volcano information:</h4>
Height: %s m
"""

html2 = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

def color_producer(el):
    if (el<2000):
        return 'green'
    elif (el<4000):
        return 'blue'
    else:
        return 'red'

fg=folium.FeatureGroup(name="Volcanoes")
for lt,ln,el in zip(lat,lon,elev):
    #simple popup
    #fg.add_child(folium.Marker(location=[lt,ln],popup=str(el),icon=folium.Icon(color='green'))) #add marker

    # use it if el contains ' or "
    #fg.add_child(folium.Marker(location=[lt,ln],popup=folium.Popup(str(el),parse_html=True), icon=folium.Icon(color='green'))) #add marker

    #make iframe with html inside
    #iframe = folium.IFrame(html=html1 % str(el), width=200, height=100)
    #fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon = folium.Icon(color =color_producer(el)) ))

    #add hyperlink inside iframe 
    #iframe = folium.IFrame(html=html2 % (name, name, el), width=200, height=100)
    #fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon = folium.Icon(color = "green")))
    
    #make iframe with html inside
    iframe = folium.IFrame(html=html1 % str(el), width=200, height=100)
    fg.add_child(folium.CircleMarker(location=[lt, ln], 
        radiud=5,color=color_producer(el),fill=True,fill_color=color_producer(el),
        popup=folium.Popup(iframe) ))

fg.add_child(folium.GeoJson(data=open("world.json","r",encoding='utf-8-sig').read()))
map.add_child(fg)

map.save("1.html") # create html file with map

