from geopy.geocoders import Nominatim
import folium

def locateCoordinates(city):
    geolocator = Nominatim(user_agent="MyApp")

    location = geolocator.geocode(city)

    return (location.latitude, location.longitude)

def drawMap(methodA, methodB):
    mapOfRomenia = folium.Map(location=(46, 25), zoom_start=7)
    mapOfCoordinatesA = []
    mapOfCoordinatesB = []
    for city in methodA["path"]:
        mapOfCoordinatesA.append(locateCoordinates(city))
    folium.PolyLine(
        mapOfCoordinatesA, 
        color = "red", 
        tooltip=methodA["searchType"]
        ).add_to(mapOfRomenia)
    for city in methodB["path"]:
        mapOfCoordinatesB.append(locateCoordinates(city))
    folium.PolyLine(
        mapOfCoordinatesB, 
        color = "green", 
        tooltip=methodB["searchType"]
        ).add_to(mapOfRomenia)
    mapOfRomenia.save("map.html")



