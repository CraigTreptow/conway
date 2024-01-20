import sys

DEFAULT_SIZE = 10
DEAD = 0
ALIVE = 1

# 0,0 is top left
# 9,9 is bottom right

def display_grid(grid):
    for row in grid:
        print("".join(" * " if cell else " . " for cell in row))

grid_size = int(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_SIZE
grid = [[DEAD for _ in range(grid_size)] for _ in range(grid_size)]
grid[0][0] = ALIVE
grid[9][9] = ALIVE

print(grid)
display_grid(grid)

print(f"Conway with {grid_size} X {grid_size} grid!")
