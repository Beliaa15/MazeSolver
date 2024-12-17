import heapq
from utils.get_neighbours_for_best_first import get_neighbours_for_best_first

def ucs_maze_solver(maze, start, end):
    """
    Solves the maze using the Uniform Cost Search algorithm.
    
    :param maze: The maze to be solved
    :param start: Starting point (row, column)
    :param end: Ending point (row, column)
    :return: The maze with the path marked
    """
    
    path = []
    visited = set()  # Use a set for faster lookups
    queue = []  # This will be a priority queue
    prev_nodes = {}  # To track the path
    cost = {}  # To track the cost to reach each node

    # Initialize the start node
    heapq.heappush(queue, (0, tuple(start)))  # (cost, (row, column))
    cost[tuple(start)] = 0

    while queue:
        # Get the node with the lowest cost
        current_cost, actual = heapq.heappop(queue)
        
        if actual in visited:
            continue  # Skip if already visited
        
        visited.add(actual)  # Mark the node as visited

        if actual == tuple(end):
            break  # Exit if we reached the end
        
        # Get valid neighbours
        neighbours = get_neighbours_for_best_first(maze, actual[0], actual[1], visited)
        
        for neighbour in neighbours:
            new_cost = current_cost + 1  # Assuming each move has a cost of 1
            if neighbour not in visited and (neighbour not in cost or new_cost < cost[neighbour]):
                cost[neighbour] = new_cost
                prev_nodes[neighbour] = actual
                heapq.heappush(queue, (new_cost, neighbour))

    # Backtrack to find the path
    actual = tuple(end)
    while actual in prev_nodes:
        path.append(actual)
        actual = prev_nodes[actual]

    path.append(tuple(start))  # Add the start node
    path.reverse()  # Reverse the path to get it from start to end
    
    # Optionally mark visited cells for visualization
    for (x, y) in visited:
        maze[x][y] = '3'  # Use '3' to represent visited cells
    
    # Mark the path in the maze with '2'
    for (x, y) in path:
        maze[x][y] = '2'  # Use '2' to represent the path

    return maze