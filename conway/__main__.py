import sys
import time
from curses import wrapper

def display_grid(window, grid):
    for index, row in enumerate(grid):
        window.addstr(index, 0, "".join(" * " if cell else " . " for cell in row))
        window.refresh()
        time.sleep(0.1)

def main(window):
    DEFAULT_SIZE = 60
    DEAD = 0
    ALIVE = 1
    grid_size = int(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_SIZE

    window.clear()
    dimensions = window.getmaxyx()
    max_y = dimensions[0]
    max_x = dimensions[1]
    if grid_size > max_y or grid_size > grid_size:
        raise Exception(f"Terminal window not large enough: Grid size: {grid_size} MaxY: {max_y} MaxX: {max_x}")
    window.refresh()

    # 0,0 is top left
    # X-1,X-1 is bottom right

    grid = [[DEAD for _ in range(grid_size)] for _ in range(grid_size)]
    grid[0][0] = ALIVE
    grid[9][9] = ALIVE
    display_grid(window, grid)
    grid[6][5] = ALIVE
    time.sleep(1)
    display_grid(window, grid)


wrapper(main)
