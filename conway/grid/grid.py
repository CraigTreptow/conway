from conway.common.constants import *

def tick(grid):
    changes = False
    new_grid = [[DEAD for _ in range(len(grid))] for _ in range(len(grid))]

    for row_index, row in enumerate(grid):
        for column_index, cell in enumerate(row):
            # Count neighbors
            neighbors = 0

            # Top left
            if row_index > 0 and column_index > 0:
                neighbors += grid[row_index - 1][column_index - 1]

            # Top
            if row_index > 0:
                neighbors += grid[row_index - 1][column_index]

            # Top right
            if row_index > 0 and column_index < len(row) - 1:
                neighbors += grid[row_index - 1][column_index + 1]

            # Left
            if column_index > 0:
                neighbors += grid[row_index][column_index - 1]

            # Right
            if column_index < len(row) - 1:
                neighbors += grid[row_index][column_index + 1]

            # Bottom left
            if row_index < len(grid) - 1 and column_index > 0:
                neighbors += grid[row_index + 1][column_index - 1]

            # Bottom
            if row_index < len(grid) - 1:
                neighbors += grid[row_index + 1][column_index]

            # Bottom right
            if row_index < len(grid) - 1 and column_index < len(row) - 1:
                neighbors += grid[row_index + 1][column_index + 1]

            if cell == ALIVE:
                if neighbors < 2:
                    changes = True
                    new_grid[row_index][column_index] = DEAD
                elif neighbors == 2 or neighbors == 3:
                    changes = True
                    new_grid[row_index][column_index] = ALIVE
                elif neighbors > 3:
                    changes = True
                    new_grid[row_index][column_index] = DEAD
            elif cell == DEAD:
                if neighbors == 3:
                    changes = True
                    new_grid[row_index][column_index] = ALIVE

    return (new_grid, changes)