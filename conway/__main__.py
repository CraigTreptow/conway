from conway.utils.util import *
from conway.grid.grid import *
from conway.common.constants import *
from curses import wrapper
import time

def main(window):
    grid = generate_grid_from_file(window)
    window.clear()

    # 0,0 is top left
    # X-1,X-1 is bottom right
    # y,x (rows down, columns right)

    flag = GracefulExiter()
    while True:
        display_grid(window, grid)
        time.sleep(1)
        (grid, changes) = tick(grid)
        if flag.exit() or changes == False:
            break


wrapper(main)
