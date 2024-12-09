import matplotlib.pyplot as plt
import numpy as np

def print_maze(maze, ax=None):
    if ax is None:
        ax = plt.gca()
    
    # Convert maze characters to numerical values
    maze_array = []
    for row in maze:
        maze_row = []
        for cell in row:
            if cell == '1':  # Wall
                maze_row.append(0.5)  # Black
            elif cell == '2':  # Path
                maze_row.append(0)  # Green
            else:  # Empty space or other characters
                maze_row.append(1)  # White
        maze_array.append(maze_row)
    
    # Create custom colormap: black for walls, white for paths, green for solution
    colors = ['green', 'white', 'black']
    cmap = plt.cm.colors.ListedColormap(colors)
    
    # Display the maze and return the image object
    ax.imshow(maze_array, cmap=cmap, interpolation='nearest')
    ax.axis('off')
    plt.show()