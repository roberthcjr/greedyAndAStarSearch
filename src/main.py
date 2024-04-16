from helpers.search import search
from shared.distancias import distanciasRodoviarias, distanciasBucharest

start = input("Enter the start node: ")
searchType = int(input("Enter the search type (greedyFirst(0) or aStar(1)): "))
goal = "Bucharest"

path, cost = search(searchType, start, goal, distanciasRodoviarias, distanciasBucharest)
path = path + [goal]

# Print the path and the cost
print("Path:", path)
print("Cost:", cost)