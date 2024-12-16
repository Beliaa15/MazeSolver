def get_neighbours_for_astar(maze, i, j, visited):
    """
    It returns the neighbours of a given cell in the maze, 
    but only if the cell is not a wall and has not been visited
    
    :param maze: The maze we're working with
    :param i: the current row
    :param j: column
    :param visited: a set of tuples that represent the coordinates of the cells that have been visited
    :return: A dictionary of tuples with their coordinates as keys and a distance of 1 as value.
    """

    neighbours = {}
    rows, cols = len(maze), len(maze[0])

    if i > 0 and maze[i - 1][j] != '0' and (i - 1, j) not in visited:
        neighbours[(i - 1, j)] = 1
    if i < rows - 1 and maze[i + 1][j] != '0' and (i + 1, j) not in visited:
        neighbours[(i + 1, j)] = 1
    if j > 0 and maze[i][j - 1] != '0' and (i, j - 1) not in visited:
        neighbours[(i, j - 1)] = 1
    if j < cols - 1 and maze[i][j + 1] != '0' and (i, j + 1) not in visited:
        neighbours[(i, j + 1)] = 1

    return neighbours
