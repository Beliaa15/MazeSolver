from collections import deque
from utils.get_neighbours_for_best_first import get_neighbours_for_best_first
from utils.get_neighbours_for_search import get_neighbours_for_search

def bfs_maze_solver(maze, start, end):
    """
    Solves the maze using the Breadth-First Search algorithm.
    
    :param maze: The maze to be solved
    :param start: Starting point (row, column)
    :param end: Ending point (row, column)
    :return: The maze with the path marked
    """
    visited = set()
    path = []
    queue = deque([tuple(start)])
    prev_nodes = {}

    while queue:
        current = queue.popleft()
        
        if current in visited:
            continue
            
        visited.add(current)
        
        if current == tuple(end):
            break
            
        neighbours = get_neighbours_for_search(maze, current[0], current[1], visited)
        
        for neighbour in neighbours:
            if neighbour not in visited:
                queue.append(neighbour)
                prev_nodes[neighbour] = current

    # Reconstruct path
    current = tuple(end)
    while current in prev_nodes:
        path.append(current)
        current = prev_nodes[current]
    
    path.append(tuple(start))
    path.reverse()

    # Mark the path
    for (x, y) in path:
        maze[x][y] = '2'

    return maze