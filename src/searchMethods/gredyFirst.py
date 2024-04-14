# Gredy Best First Search returning the path and the cost
def gredyFirstSearch(start, goal, frontiers, distancies, visited = []):
    path = []
    cost = 0

    if start == goal:
        return path, cost

    visited.append(start)
    neighbours = frontiers[start]

    minor = distancies[list(neighbours.keys())[0]]
    print(minor)
    for neighbour in neighbours:
        if neighbour not in visited:
            break

    return path, cost
    
