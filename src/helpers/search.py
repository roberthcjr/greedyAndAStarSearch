from utils.comparations import findMinorDistanceAndCity, isAStar, SEARCH_TYPES
from utils.getters import getPathAndCost


# This file contains the search function that is used to find the path between two cities
def search(searchType, start, goal, frontiers, distancies, visited = None):
    if visited is None:
        visited = []
    path = []
    cost = 0
    distanciesAux = distancies.copy()

    if start == goal:
        return {
            "path": path,
            "cost": cost,
            "searchType": SEARCH_TYPES[searchType]
        }

    visited.append(start)
    neighbours = frontiers[start]

    if isAStar(searchType):
        distanciesAux.update({
            neighbour: distancies[neighbour] + neighbours[neighbour] for neighbour in neighbours
        })

    city, minor = findMinorDistanceAndCity(neighbours, distanciesAux, visited)
    
    aux = search(searchType, city, goal, frontiers, distancies, visited)

    path, cost = getPathAndCost(searchType, start, city, minor, neighbours, aux["path"], aux["cost"])

    return {
            "path": path,
            "cost": cost,
            "searchType": SEARCH_TYPES[searchType]
        }