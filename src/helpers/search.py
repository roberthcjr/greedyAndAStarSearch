from utils.comparations import findMinorDistanceAndCity
from utils.comparations import isAStar
from utils.getters import getPathAndCost


# This file contains the search function that is used to find the path between two cities
def search(searchType, start, goal, frontiers, distancies, visited = None):
    if visited is None:
        visited = []
    path = []
    cost = 0
    distanciesAux = distancies.copy()

    if start == goal:
        return path, cost

    visited.append(start)
    neighbours = frontiers[start]

    if isAStar(searchType):
        distanciesAux.update({
            neighbour: distancies[neighbour] + neighbours[neighbour] for neighbour in neighbours
        })

    city, minor = findMinorDistanceAndCity(neighbours, distanciesAux, visited)
    
    pathAux, costAux = search(searchType, city, goal, frontiers, distancies, visited)

    path, cost = getPathAndCost(searchType, start, city, minor, neighbours, pathAux, costAux)

    return path, cost