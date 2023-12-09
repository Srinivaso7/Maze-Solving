import pygame
import random
import sys

class MazeGenerator:
    def __init__(self, rows, cols, cell_size):
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size
        self.maze = [['WALL' for _ in range(cols)] for _ in range(rows)]
        self.start_node = None
        self.goal_node = None

        pygame.init()
        self.screen = pygame.display.set_mode((cols * cell_size, rows * cell_size))
        pygame.display.set_caption("DFS Maze Generator")

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
        self.screen.fill((255, 255, 255))

        for i, row in enumerate(self.maze):
            for j, cell in enumerate(row):
                x1, y1 = j * self.cell_size, i * self.cell_size
                x2, y2 = x1 + self.cell_size, y1 + self.cell_size

                fill_color = (0, 0, 0) if cell == 'WALL' else (255, 255, 255)
                pygame.draw.rect(self.screen, fill_color, (x1, y1, x2 - x1, y2 - y1))

        # Highlight the start node
        if self.start_node:
            x, y = self.start_node
            pygame.draw.rect(self.screen, (0, 255, 0), (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))

        # Highlight the goal node
        if self.goal_node:
            x, y = self.goal_node
            pygame.draw.rect(self.screen, (255, 0, 0), (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))

        pygame.display.flip()

    def generate_and_draw_maze(self):
        self.maze = [['WALL' for _ in range(self.cols)] for _ in range(self.rows)]
        self.draw_maze()

        self.generate_dfs_maze()
        self.draw_maze()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.generate_and_draw_maze()

if __name__ == "__main__":
    rows = 50  # Adjust the number of rows
    cols = 50  # Adjust the number of columns
    cell_size = 10  # Adjust the size of each cell

    maze_generator = MazeGenerator(rows, cols, cell_size)
    maze_generator.run()
