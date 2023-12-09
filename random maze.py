import tkinter as tk
import random

class MazeGenerator:
    def __init__(self, rows, cols, cell_size):
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size
        self.maze = [['WALL' for _ in range(cols)] for _ in range(rows)]
        self.start_node = None
        self.goal_node = None

        self.root = tk.Tk()
        self.root.title("DFS Maze Generator")

        self.canvas = tk.Canvas(self.root, width=cols * cell_size, height=rows * cell_size)
        self.canvas.pack()

        self.generate_button = tk.Button(self.root, text="Generate Maze", command=self.generate_and_draw_maze)
        self.generate_button.pack()

    def is_valid(self, x, y):
        return 0 <= x < self.rows and 0 <= y < self.cols and self.maze[x][y] == 'WALL'

    def carve_path(self, x, y):
        self.maze[x][y] = 'EMPTY'

        directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if self.is_valid(nx, ny):
                self.maze[(x + nx) // 2][(y + ny) // 2] = 'EMPTY'
                self.carve_path(nx, ny)

    def generate_dfs_maze(self):
        # Start from the top-left corner
        self.carve_path(0, 0)
        self.start_node = (0, 0)

        # Randomly select the goal node
        goal_x, goal_y = random.randrange(0, self.rows, 2), random.randrange(0, self.cols, 2)
        while (goal_x, goal_y) == self.start_node:
            goal_x, goal_y = random.randrange(0, self.rows, 2), random.randrange(0, self.cols, 2)

        self.goal_node = (goal_x, goal_y)

    def draw_maze(self):
        self.canvas.delete("all")
        for i, row in enumerate(self.maze):
            for j, cell in enumerate(row):
                x1, y1 = j * self.cell_size, i * self.cell_size
                x2, y2 = x1 + self.cell_size, y1 + self.cell_size

                fill_color = 'black' if cell == 'WALL' else 'white'
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color)

        # Highlight the start node
        if self.start_node:
            x, y = self.start_node
            self.canvas.create_rectangle(x * self.cell_size, y * self.cell_size,
                                         (x + 1) * self.cell_size, (y + 1) * self.cell_size,
                                         fill='green', outline='green')
        
        # Highlight the goal node
        if self.goal_node:
            x, y = self.goal_node
            self.canvas.create_rectangle(x * self.cell_size, y * self.cell_size,
                                         (x + 1) * self.cell_size, (y + 1) * self.cell_size,
                                         fill='red', outline='red') 

        

    def generate_and_draw_maze(self):
        self.maze = [['WALL' for _ in range(self.cols)] for _ in range(self.rows)]
        self.generate_dfs_maze()
        self.draw_maze()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    rows = 75 # Adjust the number of rows
    cols = 75 # Adjust the number of columns
    cell_size = 10  # Adjust the size of each cell

    maze_generator = MazeGenerator(rows, cols, cell_size)
    maze_generator.run()
