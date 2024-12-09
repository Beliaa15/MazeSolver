import heapq

from utils.get_neighbours_for_best_first import get_neighbours_for_best_first

def best_first_maze_solver(maze, start, end):
    """
    Solves the maze using the Best-First Search algorithm.
    
    :param maze: The maze to be solved
    :param start: Starting point (row, column)
    :param end: Ending point (row, column)
    :return: The maze with the path marked
    """
    
    path = []
    visited = set()  # Use a set for faster lookups
    queue = []  # This will be a priority queue
    prev_nodes = {}  # To track the path

    # Create a heuristic for each cell
    heuristic = { (i, j): abs(end[0] - i) + abs(end[1] - j) for i in range(len(maze)) for j in range(len(maze[0])) }
    
    # Push the start node into the priority queue with its heuristic value
    heapq.heappush(queue, (heuristic[tuple(start)], tuple(start)))

    while queue:
        # Get the node with the lowest heuristic value
        current_heuristic, actual = heapq.heappop(queue)
        
        if actual in visited:
            continue  # Skip if already visited
        
        visited.add(actual)  # Mark the node as visited
        
        if actual == tuple(end):
            break  # Exit if we reached the end
        
        # Get valid neighbours
        neighbours = get_neighbours_for_best_first(maze, actual[0], actual[1], visited)
        
        for neighbour in neighbours:
            if neighbour not in visited:
                # Track the previous node for path reconstruction
                prev_nodes[neighbour] = actual
                # Push the neighbour into the priority queue with its heuristic value
                heapq.heappush(queue, (heuristic[neighbour], neighbour))

    # Backtrack to find the path
    actual = tuple(end)
    while actual in prev_nodes:
        path.append(actual)
        actual = prev_nodes[actual]

    path.append(tuple(start))  # Add the start node
    path.reverse()  # Reverse the path to get it from start to end

    # Mark the path in the maze with '2'
    for (x, y) in path:
        maze[x][y] = '2'  # Use '2' to represent the path

    return maze