from utils.get_neighbours_for_search import get_neighbours_for_search

def ids_maze_solver(maze, start, end):
    """
    Solves the maze using the Iterative Deepening Depth-First Search (IDDFS) algorithm.
    :param maze: The maze to be solved
    :param start: Starting point (row, column)
    :param end: Ending point (row, column)
    :return: The maze with the path marked
    """
    def dfs_limited(node, depth, visited, prev_nodes):
        if depth == 0 and node == tuple(end):
            return True
        if depth > 0:
            neighbours = get_neighbours_for_search(maze, node[0], node[1], visited)
            for neighbour in neighbours:
                if neighbour not in visited:
                    visited.add(neighbour)
                    visitedcells.add(neighbour)  # Add to visitedcells
                    prev_nodes[neighbour] = node
                    if dfs_limited(neighbour, depth - 1, visited, prev_nodes):
                        return True
                    visited.remove(neighbour)  # Backtrack
        return False

    def reconstruct_path(prev_nodes, start, end):
        path = []
        current = tuple(end)
        while current in prev_nodes:
            path.append(current)
            current = prev_nodes[current]
        path.append(tuple(start))
        path.reverse()
        return path

    def color_visited_cells(maze, visited):
        """
        Colors the visited cells in the maze with color '3'.
        
        :param maze: The maze to be modified
        :param visited: A set of visited cells
        """
        for cell in visited:
            maze[cell[0]][cell[1]] = '3'  # Use '3' to represent visited cells

    depth = 0
    path = []
    visitedcells = set()  # Initialize the visitedcells set
    while True:
        prev_nodes = {}
        visited = set()  # Create a new visited set for each depth iteration
        visited.add(tuple(start))
        visitedcells.add(tuple(start))  # Add the start point to visitedcells
        if dfs_limited(tuple(start), depth, visited, prev_nodes):
            path = reconstruct_path(prev_nodes, start, end)
            break
        depth += 1

    # Color the visited cells
    color_visited_cells(maze, visitedcells)
    
    # Mark the path in the maze
    for (x, y) in path:
        maze[x][y] = '2'  # Use '2' to represent the path

    return maze