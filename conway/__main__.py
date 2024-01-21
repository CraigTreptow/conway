import sys
import time
from curses import wrapper

def pbar(window):
    for i in range(10):
        window.addstr(10, 10, "[" + ("=" * i) + ">" + (" " * (10 - i )) + "]")
        window.refresh()
        time.sleep(0.5)

# def display_grid(grid):
#     for row in grid:
#         print("".join(" * " if cell else " . " for cell in row))

def display_grid(window, grid):
    for index, row in enumerate(grid):
        window.addstr(index, 0, "".join(" * " if cell else " . " for cell in row))
        window.refresh()
        time.sleep(0.5)
    # for i in range(10):
    #     window.addstr(0, 0, "[" + ("=" * i) + ">" + (" " * (10 - i )) + "]")
    #     window.refresh()
    #     time.sleep(0.5)

def main(stdscr):
    stdscr.clear()
    # 0,0 is top left
    # 9,9 is bottom right

    grid_size = int(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_SIZE
    grid = [[DEAD for _ in range(grid_size)] for _ in range(grid_size)]
    grid[0][0] = ALIVE
    grid[9][9] = ALIVE
    display_grid(stdscr, grid)
    grid[6][5] = ALIVE
    time.sleep(1)
    display_grid(stdscr, grid)


DEFAULT_SIZE = 20
DEAD = 0
ALIVE = 1

# print(grid)
# display_grid(grid)
# curses.wrapper(pbar)
wrapper(main)
