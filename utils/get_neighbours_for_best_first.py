def get_neighbours_for_best_first(maze, i, j, visited):
    """
    Returns a list of valid neighbours for the Best-First Search algorithm.
    
    :param maze: The maze we're trying to solve
    :param i: the current row
    :param j: the column of the current cell
    :param visited: a set of all the cells that have been visited
    :return: A list of neighbours that have not been visited.
    """
    neighbours = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    for di, dj in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < len(maze) and 0 <= nj < len(maze[0]) and (ni, nj) not in visited:
            # Check if the cell between the current cell and the neighbour is a path
            if maze[i + di // 2][j + dj // 2] == '1':  # Ensure there's a path
                neighbours.append((ni, nj))

    return neighbours