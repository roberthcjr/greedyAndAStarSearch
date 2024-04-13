# Import distanciasRodoviarias and distanciasBucharest from src/shared/distancias.py
# and use them in the search methods.
#
Import("distanciasRodoviarias", "distanciasBucharest") 

# Gredy Best First Search returning the path and the cost
def gredyFirstSearch(start, goal, distancias):
    # Create a priority queue
    frontier = PriorityQueue()
    # Add the start node to the queue
    frontier.put(start, 0)
    # Create a dictionary to store the cost of the path
    costSoFar = {start: 0}
    # Create a dictionary to store the path
    cameFrom = {start: None}
    # While the queue is not empty
    while not frontier.empty():
        # Get the current node
        current = frontier.get()
        # If the current node is the goal
        if current == goal:
            # Create a list to store the path
            path = []
            # Add the goal to the path
            path.append(goal)
            # While the current node is not the start node
            while current != start:
                # Get the previous node
                current = cameFrom[current]
                # Add the previous node to the path
                path.append(current)
            # Reverse the path
            path.reverse()
            # Return the path and the cost
            return path, costSoFar[goal]
        # For each neighbor of the current node
        for neighbor in distancias[current]:
            # Calculate the cost of the path
            newCost = costSoFar[current] + distancias[current][neighbor]
            # If the neighbor is not in the cost dictionary or the new cost is less than the current cost
            if neighbor not in costSoFar or newCost < costSoFar[neighbor]:
                # Update the cost dictionary
                costSoFar[neighbor] = newCost
                # Calculate the heuristic
                priority = newCost
                # Add the neighbor to the queue
                frontier.put(neighbor, priority)
                # Update the path dictionary
                cameFrom[neighbor] = current
    # Return None if the goal is not reachable
    return None, None
