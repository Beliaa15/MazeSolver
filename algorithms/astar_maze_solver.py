import math
from utils.get_neighbours_for_astar import get_neighbours_for_astar

def astar_maze_solver(maze, start, end):
    """
    It takes a maze, a start and an end, and returns the path from start to end

    :param maze: the maze to be solved
    :param start: (1, 1)
    :param end: the end point of the maze
    """
    path = []
    visited = set()
    queue = {}

    # Create a dictionary with the distance from start to each node
    distance = { (i, j): math.inf for i in range(len(maze)) for j in range(len(maze[0])) if maze[i][j] != '0' }
    distance[tuple(start)] = 0

    # Create a dictionary with the heuristic estimates
    heuristic = { (i, j): abs(end[0] - i) + abs(end[1] - j) for i in range(len(maze)) for j in range(len(maze[0])) if maze[i][j] != '0' }

    # Create a dictionary to store the previous nodes
    prev_nodes = { (i, j): None for i in range(len(maze)) for j in range(len(maze[0])) if maze[i][j] != '0' }
    
    actual = start
    queue[tuple(start)] = 0

    while queue:
        actual = min(queue, key=lambda k: queue[k] + heuristic[k])
        if actual == tuple(end):
            break
        
        current_weight = distance[actual]
        neighbours = get_neighbours_for_astar(maze, actual[0], actual[1], visited)
        coordinates_neighbours = list(neighbours.keys())
        
        for neighbour in coordinates_neighbours:
            if neighbour not in visited:
                tentative_distance = current_weight + 1
                if tentative_distance < distance[neighbour]:
                    distance[neighbour] = tentative_distance
                    prev_nodes[neighbour] = actual
                    queue[neighbour] = tentative_distance
        
        visited.add(actual)
        maze[actual[0]][actual[1]] = '3'  # Mark visited cells with '3'
        del queue[actual]

    actual = tuple(end)
    while actual:
        path.append(actual)
        actual = prev_nodes[actual]
    
    path.reverse()

    for i in range(len(path)):
        if i < len(path) - 1:
            actual = path[i]
            next = path[i+1]
            if actual[0] == next[0]:
                maze[actual[0]][actual[1] + (1 if actual[1] < next[1] else -1)] = '2'
            elif actual[1] == next[1]:
                maze[actual[0] + (1 if actual[0] < next[0] else -1)][actual[1]] = '2'
        maze[path[i][0]][path[i][1]] = '2'

    return maze
