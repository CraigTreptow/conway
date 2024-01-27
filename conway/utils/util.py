import argparse
from conway.common.constants import *
import fileinput
import signal

def display_grid(window, grid):
    for index, row in enumerate(grid):
        window.addstr(index, 0, "".join(" * " if cell else " . " for cell in row))
        # window.addstr(index, 0, "".join(" * " if cell else "   " for cell in row))
        window.refresh()

def generate_grid_from_file(window):
    parser = argparse.ArgumentParser()                                               
    parser.add_argument("--file", "-f", type=str, required=True)
    args = parser.parse_args()
    grid = []

    with open(args.file, "r") as f:
        data = f.read()
        lines = data.splitlines()

    for index, line in enumerate(lines):
        if index == 0:
            grid_size = int(line)
            dimensions = window.getmaxyx()
            max_y = dimensions[0]
            max_x = dimensions[1]

            if grid_size > max_y or grid_size > grid_size:
                raise Exception(f"Terminal window not large enough: Grid size: {grid_size} MaxY: {max_y} MaxX: {max_x}")

            grid = [[DEAD for _ in range(grid_size)] for _ in range(grid_size)]
        elif "#" in line:
            pass
        else:
            x, y = line.split(",")
            x = int(x)
            y = int(y)
            grid[x][y] = ALIVE

    return grid

class GracefulExiter():
    def __init__(self):
        self.state = False
        signal.signal(signal.SIGINT, self.change_state)

    def change_state(self, signum, frame):
        print("exit flag set to True (repeat to exit now)")
        signal.signal(signal.SIGINT, signal.SIG_DFL)
        self.state = True

    def exit(self):
        return self.state
