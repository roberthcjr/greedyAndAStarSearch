from helpers.search import search
from shared.distancias import distanciasRodoviarias, distanciasBucharest
from helpers.map import drawMap, openMap

start = input("Digite a cidade de origem: ")
while start not in distanciasBucharest:
    start = input("Cidade não encontrada, digite outra: ")
goal = "Bucharest"

greedy = search(0, start, goal, distanciasRodoviarias, distanciasBucharest)
greedy["path"] += [goal]  

aStar = search(1, start, goal, distanciasRodoviarias, distanciasBucharest)
aStar["path"] += [goal]

drawMap(greedy, aStar, start, goal)

# Print the path and the cost
print("O caminho feito pelo método guloso:", greedy["path"])
print("A distância calculada do método guloso:", greedy["cost"])

print("O caminho feito pelo método A*:", aStar["path"])
print("A distância calculada do método A*:", aStar["cost"])

openMap()