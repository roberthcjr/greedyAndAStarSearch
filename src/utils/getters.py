from utils.comparations import isAStar

def getPathAndCost(searchType, start, city, minor, neighbours, pathAux, costAux):
    cost = 0
    path = [start] + pathAux
    if isAStar(searchType):
        cost += neighbours[city] + costAux
    else:
        cost += minor + costAux
    return path, cost