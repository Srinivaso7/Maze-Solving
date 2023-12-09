import tkinter as tk
import random

def generate_maze(rows, cols):
    maze = [['WALL' for _ in range(cols)] for _ in range(rows)]

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols and maze[x][y] == 'WALL'

    def carve_path(x, y):
        maze[x][y] = 'EMPTY'

        directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny):
                maze[(x + nx) // 2][(y + ny) // 2] = 'EMPTY'
                carve_path(nx, ny)

    start_x, start_y = random.randrange(0, rows, 2), random.randrange(0, cols, 2)
    carve_path(start_x, start_y)

    return maze

def draw_maze(canvas, maze, cell_size):
    canvas.delete("all")
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            x1, y1 = j * cell_size, i * cell_size
            x2, y2 = x1 + cell_size, y1 + cell_size

            if cell == 'WALL':
                canvas.create_rectangle(x1, y1, x2, y2, fill='black')
            else:
                canvas.create_rectangle(x1, y1, x2, y2, fill='white')

def generate_and_draw_maze(rows, cols, cell_size):
    maze = generate_maze(rows, cols)
    draw_maze(canvas, maze, cell_size)

if __name__ == "__main__":
    rows = 9  # Adjust the number of rows
    cols = 9  # Adjust the number of columns
    cell_size = 30  # Adjust the size of each cell

    root = tk.Tk()
    root.title("Maze Generator")

    canvas = tk.Canvas(root, width=cols * cell_size, height=rows * cell_size)
    canvas.pack()

    generate_and_draw_maze(rows, cols, cell_size)

    root.mainloop()
