import folium
import pandas

# load data
data = pandas.read_csv("Volcanoes.txt")

# store data from columns in data to lists

latitude = list(data["LAT"])
longitude = list(data["LON"])

map = folium.Map(location=[80, -100], zoom_start=6, tiles="MapBox Bright")

fg = folium.FeatureGroup(name="My Map")

# add multitle markers
for lt, lg in zip(latitude, longitude):
    fg.add_child(folium.Marker(location=[lt, lg], popup="Hi Im a marker", icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("Map1.html")