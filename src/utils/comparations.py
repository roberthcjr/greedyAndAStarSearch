SEARCH_TYPES = ["greedyFirst", "aStar"]

def isAStar(searchType):
    return SEARCH_TYPES[searchType] == SEARCH_TYPES[1]


def findMinorDistanceAndCity(neighbours, distancies, visited = []):
    city = list(neighbours.keys())[0]

    minor = distancies[city]
    for neighbour in neighbours:
        if neighbour not in visited and neighbour != city:
            if distancies[neighbour] < minor:
                city = neighbour
                minor = distancies[neighbour]

    return city, minor