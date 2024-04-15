from searchMethods.greedyFirst import greedyFirstSearch
from shared.distancias import distanciasRodoviarias, distanciasBucharest

start = input("Enter the start node: ")
goal = "Bucharest"

# Call the Greedy Best First Search function
path, cost = greedyFirstSearch(start, goal, distanciasRodoviarias, distanciasBucharest)
path = path + [goal]

# Print the path and the cost
print("Path:", path)
print("Cost:", cost)