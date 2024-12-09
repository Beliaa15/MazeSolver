import time
import matplotlib.pyplot as plt
from matplotlib.widgets import RadioButtons

# Utils
from utils.generate_grid import generate_grid
from utils.print_maze import print_maze
from utils.carve import carve
from utils.modify import modify

# Algorithms
from algorithms.dfs_maze_solver import dfs_maze_solver
from algorithms.bfs_maze_solver import bfs_maze_solver
from algorithms.dijkstra_maze_solver import dijkstra_maze_solver
from algorithms.astar_maze_solver import astar_maze_solver

class MazePresentation:
    def __init__(self):
        self.m = 41
        self.n = 41
        self.solutions = self.generate_solutions()
        
    def generate_solutions(self):
        maze = []
        solutions = []

        # Generate and prepare maze
        maze = generate_grid(self.n, self.m, maze)
        carve(maze)
        modify(maze, self.m, self.n)

        algorithms = [
            ('DFS', dfs_maze_solver),
            ('BFS', bfs_maze_solver),
            ('Dijkstra', dijkstra_maze_solver),
            ('A*', astar_maze_solver)
        ]

        for name, solver in algorithms:
            maze_copy = [row[:] for row in maze]
            start_time = time.time()
            solver(maze_copy, [1, 1], [self.m-2, self.n-2])
            execution_time = time.time() - start_time
            solutions.append({
                'maze': maze_copy,
                'name': name,
                'time': execution_time
            })

        return solutions

    def show_solutions(self):
        fig, ax = plt.subplots(figsize=(12, 10))
        plt.subplots_adjust(left=0.2)  # space for radio buttons
        
        # radio buttons
        rax = plt.axes([0.05, 0.4, 0.15, 0.15])  # [left, bottom, width, height]
        radio = RadioButtons(rax, ['DFS', 'BFS', 'Dijkstra', 'A*'])
        
        def update_plot(label):
            ax.clear()
            index = next(i for i, sol in enumerate(self.solutions) if sol['name'] == label)
            solution = self.solutions[index]
            ax.set_title(f"{solution['name']} Solution\nExecution time: {solution['time']:.6f} seconds")
            print_maze(solution['maze'], ax=ax)
            plt.draw()
        
        # initial solution
        update_plot('DFS')
        radio.on_clicked(update_plot)
        print("Plot changed")
        plt.show()

def main():
    presentation = MazePresentation()
    presentation.show_solutions()

if __name__ == "__main__":
    main()