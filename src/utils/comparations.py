SEARCH_TYPES = ["greedyFirst", "aStar"]

def isAStar(searchType):
    return SEARCH_TYPES[searchType] == SEARCH_TYPES[1]


def findMinorDistanceAndCity(neighbours, distancies, visited):
    city = None
    min_distance = float('inf')

    for neighbor in neighbours:
        if neighbor not in visited:
            if distancies[neighbor] < min_distance:
                city = neighbor
                min_distance = distancies[neighbor]

    return city, min_distance