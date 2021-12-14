import folium
import gpxpy
import gpxpy.gpx
import sys

if len(sys.argv)<=1:
    print ("usage: gpx2map.py <file.gpx>")
    exit(0)

gpx_file = open(sys.argv[1], 'r')
gpx = gpxpy.parse(gpx_file)


for track in gpx.tracks:
    print (track.name)
    for segment in track.segments:
        for point in segment.points:
            print('Point at ({0},{1}) -> {2}'.format(point.latitude, point.longitude, point.elevation))

for waypoint in gpx.waypoints:
    print('waypoint {0} -> ({1},{2})'.format(waypoint.name, waypoint.latitude, waypoint.longitude))

for route in gpx.routes:
    print('Route:')
    for point in route.points:
        print('routePoint at ({0},{1}) -> {2}'.format(point.latitude, point.longitude, point.elevation))

map=folium.Map(location=[0,0],tiles = "Stamen Terrain",zoom_start=10)

map_center=[]

if gpx.waypoints is not None and len(gpx.waypoints)>0:
    fg_waypoints=folium.FeatureGroup(name="waypoints")
    for waypoint in gpx.waypoints:
        map_center.append([waypoint.latitude,waypoint.longitude])
        fg_waypoints.add_child(folium.Marker(location=[waypoint.latitude,waypoint.longitude],
                                              popup=str(waypoint.name),
                                              icon=folium.Icon(color='green')
                                            )
                                ) 
    map.add_child(fg_waypoints)


if gpx.tracks is not None and len(gpx.tracks)>0:
    fg_tracks=folium.FeatureGroup(name="tracks")
    for track in gpx.tracks:
        path=[]
        for segment in track.segments:
            for point in segment.points:
                map_center.append([point.latitude,point.longitude])
                path.append((point.latitude, point.longitude))
        fg_tracks.add_child(folium.vector_layers.PolyLine(path, popup=str(track.name), tooltip=None))
    map.add_child(fg_tracks)

if gpx.routes is not None and len(gpx.routes)>0:
    fg_routes=folium.FeatureGroup(name="routes")
    for route in gpx.routes:
        for point in route.points:
            map_center.append([point.latitude,point.longitude])
            fg_routes.add_child(folium.Marker(location=[point.latitude,point.longitude],
                                              popup=str(point.name),
                                              icon=folium.Icon(color='blue')
                                              )
                                )
    map.add_child(fg_routes)

def calc_map_center(array):
    n=len(array)
    if n==0:
        return [0,0]
    else:
        x,y=0,0
        for p in array:
            x+=p[0]
            y+=p[1]
        return [x/n,y/n]

map.location=calc_map_center(map_center)
map.add_child(folium.LayerControl())  # add after feature groups

map.save("2.html") 
gpx_file.close()
