import os
import webbrowser
import folium
from shared.coordinates import coordinatesRomenia

def locateCoordinates(city):
    location = coordinatesRomenia[city]
    return (location[0], location[1])

def drawMap(methodA, methodB, fromCity, toCity):
    mapOfRomenia = folium.Map(location=(46, 25), zoom_start=7)
    mapOfCoordinatesA = [locateCoordinates(city) for city in methodA["path"]]
    mapOfCoordinatesB = [locateCoordinates(city) for city in methodB["path"]]
    folium.PolyLine(
        mapOfCoordinatesA, 
        color = "red", 
        tooltip=methodA["searchType"]
        ).add_to(mapOfRomenia)
    folium.PolyLine(
        mapOfCoordinatesB, 
        color = "green", 
        tooltip=methodB["searchType"]
        ).add_to(mapOfRomenia)
    folium.Marker(
        location=locateCoordinates(fromCity),
        popup=fromCity,
        icon=folium.Icon(color="black")
    ).add_to(mapOfRomenia)
    folium.Marker(
        location=locateCoordinates(toCity),
        popup=toCity,
        icon=folium.Icon(color="blue")
    ).add_to(mapOfRomenia)
    mapOfRomenia.save("map.html")

def openMap(): 
    filePath = 'file://' + os.path.realpath("map.html")
    new = 2
    webbrowser.open(filePath, new=new)



