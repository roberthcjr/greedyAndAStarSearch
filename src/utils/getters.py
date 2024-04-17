def getPathAndCost(searchType, start, city, minor, neighbours, pathAux, costAux):
    path = [start] + pathAux
    cost = neighbours[city] + costAux
    return path, cost