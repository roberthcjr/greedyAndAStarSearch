def getPathAndCost(start, city, neighbours, pathAux, costAux):
    path = [start] + pathAux
    cost = neighbours[city] + costAux
    return path, cost