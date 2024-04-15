def findMinorDistanceAndCity(neighbours, distancies, visited = []):
    city = list(neighbours.keys())[0]
    minor = distancies[city]
    for neighbour in neighbours:
        if neighbour not in visited and neighbour != city:
            if distancies[neighbour] < minor:
                city = neighbour
                minor = distancies[neighbour]

    return city, minor

# Gredy Best First Search returning the path and the cost
def greedyFirstSearch(start, goal, frontiers, distancies, visited = []):
    path = []
    cost = 0

    if start == goal:
        return path, cost

    visited.append(start)
    neighbours = frontiers[start]

    city, minor = findMinorDistanceAndCity(neighbours, distancies, visited)
    
    pathAux, costAux = greedyFirstSearch(city, goal, frontiers, distancies, visited)

    path += [start] + pathAux
    cost += minor + costAux

    return path, cost
    
