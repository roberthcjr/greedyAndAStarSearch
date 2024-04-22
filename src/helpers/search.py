from utils.comparations import findCityWithMinDistance, isAStar, SEARCH_TYPES
from utils.getters import getPathAndCost


# This file contains the search function that is used to find the path between two cities
def search(searchType, start, goal, frontiers, distancies, visited = None):
    path = []
    cost = 0
    if start == goal:
        return {
            "path": path,
            "cost": cost,
            "searchType": SEARCH_TYPES[searchType]
        }
    
    if visited is None:
        visited = []
    distanciesAux = distancies.copy()

    visited.append(start)
    neighbours = frontiers[start]

    if isAStar(searchType):
        distanciesAux.update({
            neighbour: distancies[neighbour] + neighbours[neighbour] for neighbour in neighbours
        })

    city = findCityWithMinDistance(neighbours, distanciesAux, visited)
    
    aux = search(searchType, city, goal, frontiers, distancies, visited)

    path, cost = getPathAndCost(start, city, neighbours, aux["path"], aux["cost"])

    return {
            "path": path,
            "cost": cost,
            "searchType": SEARCH_TYPES[searchType]
        }