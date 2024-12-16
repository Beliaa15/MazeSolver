from utils.get_neighbours_for_search import get_neighbours_for_search

def dfs_maze_solver(maze, start, end):
    """
    Solves the maze using the Depth-First Search algorithm.
    
    :param maze: The maze to be solved
    :param start: Starting point (row, column)
    :param end: Ending point (row, column)
    :return: The maze with the path marked
    """
    visited = set()
    path = []
    stack = [tuple(start)]
    prev_nodes = {}

    while stack:
        current = stack.pop()
        
        if current in visited:
            continue
            
        visited.add(current)
        maze[current[0]][current[1]] = '3'  # Mark visited cells with '3'
        
        if current == tuple(end):
            break
            
        neighbours = get_neighbours_for_search(maze, current[0], current[1], visited)
        
        for neighbour in neighbours:
            if neighbour not in visited:
                stack.append(neighbour)
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