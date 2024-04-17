import os
from helpers.search import search
from shared.distancias import distanciasRodoviarias, distanciasBucharest
from helpers.map import drawMap
import webbrowser

start = input("Enter the start node: ")
goal = "Bucharest"

greedy = search(0, start, goal, distanciasRodoviarias, distanciasBucharest)
greedy["path"] += [goal]  

aStar = search(1, start, goal, distanciasRodoviarias, distanciasBucharest)
aStar["path"] += [goal]

drawMap(greedy, aStar)

# Print the path and the cost
print("O caminho feito pelo método guloso:", greedy["path"])
print("A distância calculada do método guloso:", greedy["cost"])

print("O caminho feito pelo método A*:", aStar["path"])
print("A distância calculada do método A*:", aStar["cost"])

filePath = 'file://' + os.path.realpath("map.html")
new = 2

webbrowser.open(filePath, new=new)