import matplotlib.pyplot as plt
import numpy as np

def print_maze(maze):
    """
    Displays the maze graphically using matplotlib
    
    :param maze: The maze to display
    """
    # Convert maze to numeric values for plotting
    maze_array = np.zeros((len(maze), len(maze[0])))
    
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == '0':  # Wall
                maze_array[i][j] = 0
            elif maze[i][j] == '1':  # Path
                maze_array[i][j] = 1
            elif maze[i][j] == '2':  # Solution path
                maze_array[i][j] = 2

    # Create color map
    colors = ['black', 'white', 'green']
    cmap = plt.cm.colors.ListedColormap(colors)

    # Display the maze
    plt.imshow(maze_array, cmap=cmap)
    plt.axis('off')