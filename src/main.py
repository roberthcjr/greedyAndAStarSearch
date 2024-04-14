from searchMethods.gredyFirst import gredyFirstSearch
from shared.distancias import distanciasRodoviarias, distanciasBucharest

# Define the start and goal nodes
start = "Arad"
goal = "Bucharest"

# Call the Gredy Best First Search function
path, cost = gredyFirstSearch(start, goal, distanciasRodoviarias, distanciasBucharest)

# Print the path and the cost
print("Path:", path)
print("Cost:", cost)