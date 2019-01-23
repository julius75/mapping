import folium
import pandas

# load data
data = pandas.read_csv("Volcanoes.txt")

# store data from columns in data to lists

latitude = list(data["LAT"])
longitude = list(data["LON"])
elevation = list(data["ELEV"])

# function for evevation


def color_elevation(elevations):
    if elevations > 1000:
        return 'green'
    elif 1000 <= elevations > 3000:
        return 'orange'
    else:
        return 'red'


map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="MapBox Bright")

fg = folium.FeatureGroup(name="My Map")

# add multitle markers
for lt, lg, el in zip(latitude, longitude, elevation):
    fg.add_child(folium.Marker(location=[lt, lg], popup=str(el) + " m", icon=folium.Icon(color=color_elevation(el))))

map.add_child(fg)

map.save("Map1.html")