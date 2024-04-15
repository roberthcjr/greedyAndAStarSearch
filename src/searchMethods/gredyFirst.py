# Gredy Best First Search returning the path and the cost
def gredyFirstSearch(start, goal, frontiers, distancies, visited = []):
    path = []
    cost = 0

    if start == goal:
        return path, cost

    visited.append(start)
    neighbours = frontiers[start]

    city = list(neighbours.keys())[0]
    minor = distancies[city]
    for neighbour in neighbours:
        if neighbour not in visited and neighbour != city:
            if distancies[neighbour] < minor:
                city = neighbour
                minor = distancies[neighbour]
    
    pathAux, costAux = gredyFirstSearch(city, goal, frontiers, distancies, visited)

    path += [start] + pathAux
    cost += minor + costAux

    return path, cost
    
