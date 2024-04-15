from searchMethods.greedyFirst import greedyFirstSearch
from shared.distancias import distanciasRodoviarias, distanciasBucharest

# Define the start and goal nodes
start = "Arad"
goal = "Bucharest"

# Call the Greedy Best First Search function
path, cost = greedyFirstSearch(start, goal, distanciasRodoviarias, distanciasBucharest)

# Print the path and the cost
print("Path:", path)
print("Cost:", cost)