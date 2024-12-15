import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
from utils.generate_grid import generate_grid
from utils.carve import carve
from utils.modify import modify
from algorithms.dfs_maze_solver import dfs_maze_solver
from algorithms.bfs_maze_solver import bfs_maze_solver
from algorithms.dijkstra_maze_solver import dijkstra_maze_solver
from algorithms.astar_maze_solver import astar_maze_solver
from algorithms.best_first_search import best_first_maze_solver
from algorithms.ucs_maze_solver import ucs_maze_solver
import time

class MazeSolverGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Maze Solver")
        
        # Maze parameters
        self.m = 41
        self.n = 41
        self.maze = None
        self.cell_size = 12
        
        # Start and end points
        self.start_point = [1, 1]
        self.end_point = [self.m-2, self.n-2]
        self.placing_start = False
        self.placing_end = False
        
        # Create GUI elements
        self.create_widgets()
        
        # Generate initial maze
        self.generate_new_maze()

    def create_widgets(self):
        # Top frame for controls
        control_frame = ttk.Frame(self.root, padding="5")
        control_frame.grid(row=0, column=0, sticky="ew")
        
        # Algorithm selection
        ttk.Label(control_frame, text="Algorithm:").pack(side=tk.LEFT, padx=5)
        self.algorithm = tk.StringVar(value="DFS")
        algorithms = ["DFS", "BFS", "Dijkstra", "A*", "Best-First", "UCS"]
        algo_menu = ttk.Combobox(control_frame, textvariable=self.algorithm, values=algorithms)
        algo_menu.pack(side=tk.LEFT, padx=5)
        
        # Buttons
        ttk.Button(control_frame, text="New Maze", command=self.generate_new_maze).pack(side=tk.LEFT, padx=5)
        ttk.Button(control_frame, text="Set Start", command=self.toggle_start_placement).pack(side=tk.LEFT, padx=5)
        ttk.Button(control_frame, text="Set End", command=self.toggle_end_placement).pack(side=tk.LEFT, padx=5)
        ttk.Button(control_frame, text="Solve", command=self.solve_maze).pack(side=tk.LEFT, padx=5)
        
        # Canvas for maze display
        canvas_width = self.n * self.cell_size
        canvas_height = self.m * self.cell_size
        self.canvas = tk.Canvas(self.root, width=canvas_width, height=canvas_height, bg='white')
        self.canvas.grid(row=1, column=0, padx=10, pady=10)
        self.canvas.bind("<Button-1>", self.on_canvas_click)
        
        # Status label
        self.status_label = ttk.Label(self.root, text="")
        self.status_label.grid(row=2, column=0, pady=5)

    def toggle_start_placement(self):
        self.placing_start = not self.placing_start
        self.placing_end = False
        if self.placing_start:
            self.status_label.config(text="Click to place start point")
        else:
            self.status_label.config(text="")

    def toggle_end_placement(self):
        self.placing_end = not self.placing_end
        self.placing_start = False
        if self.placing_end:
            self.status_label.config(text="Click to place end point")
        else:
            self.status_label.config(text="")

    def on_canvas_click(self, event):
        # Convert canvas coordinates to maze indices
        i = event.y // self.cell_size
        j = event.x // self.cell_size
        
        if self.maze[i][j] == '0':
            messagebox.showerror("Invalid Position", "Cannot place point on wall")
            return
            
        if self.placing_start:
            self.start_point = [i, j]
            self.placing_start = False
            self.status_label.config(text="Start point set")
        elif self.placing_end:
            self.end_point = [i, j]
            self.placing_end = False
            self.status_label.config(text="End point set")
            
        self.draw_maze(self.maze)

    def draw_maze(self, maze):
        self.canvas.delete("all")
        for i in range(len(maze)):
            for j in range(len(maze[0])):
                x1 = j * self.cell_size
                y1 = i * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                
                if [i, j] == self.start_point:
                    color = 'blue'
                elif [i, j] == self.end_point:
                    color = 'red'
                elif maze[i][j] == '0':
                    color = 'black'
                elif maze[i][j] == '2':
                    color = 'green'
                else:
                    color = 'white'
                    
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline='')

    def generate_new_maze(self):
        self.maze = []
        self.maze = generate_grid(self.n, self.m, self.maze)
        carve(self.maze)
        modify(self.maze, self.m, self.n)
        self.draw_maze(self.maze)
        self.status_label.config(text="New maze generated")

    def solve_maze(self):
        if self.maze is None:
            return
            
        maze_copy = self.maze.copy()
        
        start_time = time.time()
        
        if self.algorithm.get() == "DFS":
            dfs_maze_solver(maze_copy, self.start_point, self.end_point)
        elif self.algorithm.get() == "BFS":
            bfs_maze_solver(maze_copy, self.start_point, self.end_point)
        elif self.algorithm.get() == "Dijkstra":
            dijkstra_maze_solver(maze_copy, self.start_point, self.end_point)
        elif self.algorithm.get() == "A*":
            astar_maze_solver(maze_copy, self.start_point, self.end_point)
        elif self.algorithm.get() == "Best-First":
            best_first_maze_solver(maze_copy, self.start_point, self.end_point)
        else:
            ucs_maze_solver(maze_copy, self.start_point, self.end_point)
            
        execution_time = time.time() - start_time
        self.draw_maze(maze_copy)
        self.status_label.config(text=f"Solved using {self.algorithm.get()} in {execution_time:.6f} seconds")

def main():
    root = tk.Tk()
    app = MazeSolverGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
