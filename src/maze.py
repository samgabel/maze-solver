from graphics import Window
from cell import Cell
import time, random


class Maze:
    def __init__(self, x1: int, y1: int, num_rows: int, num_cols: int, cell_size_x: int, cell_size_y: int, win: Window | None, seed: int | None = None):
        """
        Render in a maze grid (a matrix of Cell objects) based on the parameters listed below

        Parameters:
        `x1` , `y1` : declare the padding from the top left corner of the ui popup
        `num_rows` , `num_cols` : how big is the maze in terms of number of cells in the matrix
        `cell_size_x` , `cell_size_y` : how big is each of the cells in the matrix
        `win` : the window object, or optionally set `win=None` for testing
        `seed` : if not specified, the seed will be randomized, set `seed=0` for testing
        """

        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._seed = random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_through_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        # create matrix of cells where `_num_col` are the num of `Cell` in the inner list and `_num_row` are the num of inner lists
        self._cells = [[Cell(self._win) for _ in range(self._num_cols)] for _ in range(self._num_rows)]

        # run the `_draw_cells` method for each cell in the matrix (with respect to the (i, j) position in the matrix)
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._draw_cell(i, j)

    def _draw_cell(self, i: int, j: int):
        # don't continue to render ui when win=None (for testing purposes)
        if self._win is None:
            return

        # calculate the position of the top left cell point relative to the initial maze potition offest and the size of the cells
        x1 = (j * self._cell_size_x) + self._x1  # j is the number of cols, which is x
        y1 = (i * self._cell_size_y) + self._y1  # i is the number of rows, which is y

        # calculate the position of the bottom right cell point relative to x1 and y1
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y

        # draw the cell and animate the each object creation on the window canvas
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        # don't continue to render ui when win=None (for testing purposes)
        if self._win is None:
            return

        # refresh ui screen after every `_draw_cell` method call
        self._win.redraw()
        time.sleep(0.03)

    def _break_entrance_and_exit(self):
        # set the proper state of the entrace and exit Cell objects
        self._cells[0][0].has_top_wall = False
        self._cells[-1][-1].has_bottom_wall = False

        # redraw the entrace and exit cells
        self._draw_cell(0, 0)
        self._draw_cell(self._num_rows - 1, self._num_cols - 1)

    def _break_through_walls_r(self, i: int, j: int):
        # we essentially just want to visit all the Cells in the matrix, randomly
        self._cells[i][j].visited = True
        while True:
            # list to store available Cell directions
            to_visit = []

            # figure out what cells are available to go to and append to list
            if j > 0 and self._cells[i][j - 1].visited == False:
                to_visit.append([i, j - 1])
            if i > 0 and self._cells[i - 1][j].visited == False:
                to_visit.append([i - 1, j])
            if j < self._num_cols - 1 and self._cells[i][j + 1].visited == False:
                to_visit.append([i, j + 1])
            if i < self._num_rows - 1 and self._cells[i + 1][j].visited == False:
                to_visit.append([i + 1, j])

            # we only break the loop if there is nowhere left to go (breaks DFS traversal)
            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return

            # randomly decide which cell indices to go to out of `to_visit` indices
            direction_idx = random.randrange(len(to_visit))
            next_idx = to_visit[direction_idx]

            # knock down the walls betweeen the current and chosen cells
            diff_x = next_idx[1] - j  # 1 means new cell to the right / -1 means new cell to the left
            diff_y = next_idx[0] - i  # 1 means new cell below        / -1 means new cell above
            if diff_x == 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i][j + 1].has_left_wall = False
            if diff_x == -1:
                self._cells[i][j].has_left_wall = False
                self._cells[i][j - 1].has_right_wall = False
            if diff_y == 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i + 1][j].has_top_wall = False
            if diff_y == -1:
                self._cells[i][j].has_top_wall = False
                self._cells[i - 1][j].has_bottom_wall = False

            # recursively call the new cell
            self._break_through_walls_r(next_idx[0], next_idx[1])

    def _reset_cells_visited(self):
        for row in self._cells:
            for cell in row:
                cell.visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i: int, j: int):
        self._animate()

        # mark the current Cell as visited
        self._cells[i][j].visited = True

        # if the end is found start the coil up by returning True
        if i == self._num_rows - 1 and j == self._num_cols - 1:
            return True

        # left
        if j > 0 and self._cells[i][j - 1].visited == False and self._cells[i][j].has_left_wall == False:
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j - 1], undo=True)
        # up
        if i > 0 and self._cells[i - 1][j].visited == False and self._cells[i][j].has_top_wall == False:
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i - 1][j], undo=True)
        # right
        if j < self._num_cols - 1 and self._cells[i][j + 1].visited == False and self._cells[i][j].has_right_wall == False:
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j + 1], undo=True)
        # down
        if i < self._num_rows - 1 and self._cells[i + 1][j].visited == False and self._cells[i][j].has_bottom_wall == False:
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i + 1][j], undo=True)

        return False

