# conway
Python implementation of Conway's game of life

## To Do

- [ ] Create a grid
- [ ] Display the grid
- [ ] Read file of starting positions
- [ ] Apply starting positions to grid
- [ ] Implement rules
- [ ] Display next generation

## Description

The universe of the Game of Life is an infinite, two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, live or dead (or populated and unpopulated, respectively). Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:

1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
1. Any live cell with two or three live neighbours lives on to the next generation.
1. Any live cell with more than three live neighbours dies, as if by overpopulation.
1. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

The initial pattern constitutes the seed of the system. The first generation is created by applying the above rules simultaneously to every cell in the seed, live or dead; births and deaths occur simultaneously, and the discrete moment at which this happens is sometimes called a tick.[nb 1] Each generation is a pure function of the preceding one. The rules continue to be applied repeatedly to create further generations.


## Usage

```python -m conway grid_size```

## Setup Commands 

_create virtual environment_
`python3 -m venv venv`

_activate virtual environment_
`source venv/bin/activate`

_Note:_ To deactivate the virtual environment, simply type `deactivate` in the terminal.
_Note:_ To delete the virtual environment, simply delete the `venv` folder.
_Note:_ The above requires the  `bash`shell. If you are using `zsh` or `fish` or any other shell, please refer to the [official documentation](https://docs.python.org/3/library/venv.html) for the appropriate commands.


### zsh with oh_my_zsh setup

1. Add `virtualenv` to plugins list: `plugins=(virtualenv)`
1. Add plugin to theme prompt elements (I use powerlevel10k theme):
1. Example:
  ```
  # The list of segments shown on the left. Fill it with the most important segments.
  typeset -g POWERLEVEL9K_LEFT_PROMPT_ELEMENTS=(
    # os_icon               # os identifier
    dir                     # current directory
    vcs                     # git status
    virtualenv              # python venv
    # prompt_char           # prompt symbol
  )
  ```

## pip Commands

`pip install -r requirements.txt`
