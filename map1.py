import folium
map = folium.Map(location=[38.759, -9.115], zoom_start=12, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

for coordinates in [[38.750, -9.119],[38.740, -9.119],[38.737, -9.121],[38.747, -9.130],[38.755, -9.125],[38.751, -9.121]]:
  fg.add_child(folium.Marker(location=coordinates, popup="Hi I am a Marker", icon=folium.Icon(color='green')))
map.add_child(fg)

map.save("Map1.html")