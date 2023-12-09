import pygame
import random
import sys

# Initialize Pygame
# pygame.init()

# Maze dimensions
width = 15
height = 15

# Set up the screen
screen_size = (735, 735)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Maze Generator')

# Define cell class
class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.visited = False
        self.walls = [True, True, True, True]  # Left, Right, Up, Down

    def get_neighbors(self, grid):
        a = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Surrounding squares
        neighbors = []

        for x, y in a:
            if self.x + x in range(width) and self.y + y in range(height):
                neighbor = grid[self.y + y][self.x + x]
                if not neighbor.visited:
                    neighbors.append(neighbor)

        return neighbors

    def show(self, cell_size):
        x = self.x * cell_size
        y = self.y * cell_size

        if self.walls[0]:
            pygame.draw.line(screen, (255, 255, 255), (x, y), (x, y + cell_size))
        if self.walls[1]:
            pygame.draw.line(screen, (255, 255, 255), (x + cell_size, y), (x + cell_size, y + cell_size))
        if self.walls[2]:
            pygame.draw.line(screen, (255, 255, 255), (x, y), (x + cell_size, y))
        if self.walls[3]:
            pygame.draw.line(screen, (255, 255, 255), (x, y + cell_size), (x + cell_size, y + cell_size))

    def mark(self, cell_size):
        x = self.x * cell_size
        y = self.y * cell_size
        pygame.draw.rect(screen, (255, 0, 0), (x, y, cell_size, cell_size))

# Function to remove walls between two cells
def remove_walls(current, choice):
    if choice.x > current.x:
        current.walls[1] = False
        choice.walls[0] = False
    elif choice.x < current.x:
        current.walls[0] = False
        choice.walls[1] = False
    elif choice.y > current.y:
        current.walls[3] = False
        choice.walls[2] = False
    elif choice.y < current.y:
        current.walls[2] = False
        choice.walls[3] = False

# Function to fill corners
def corner_fill(cell_size):
    for x in range(width + 1):
        for y in range(height + 1):
            pygame.draw.rect(screen, (20, 20, 20), (x * cell_size, y * cell_size, cell_size, cell_size))

# Generate Maze
grid = [[Cell(x, y) for x in range(width)] for y in range(height)]
current = grid[0][0]
stack = []

screen.fill((210, 210, 210))

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Draw walls
    for x in range(width):
        for y in range(height):
            grid[x][y].show(screen_size[0] // width)
    
    # Fill corners
    corner_fill(screen_size[0] // width)

    current.visited = True
    current.mark(screen_size[0] // width)

    neighbors = current.get_neighbors(grid)
    if neighbors:
        choice = random.choice(neighbors)
        choice.visited = True

        stack.append(current)

        remove_walls(current, choice)

        current = choice

    elif stack:
        current = stack.pop()

    pygame.display.flip()
    screen.fill((210, 210, 210))
    pygame.time.wait(10)
