from graphics import Window
from cell import Cell
import time


class Maze:
    def __init__(self, x1: int, y1: int, num_rows: int, num_cols: int, cell_size_x: int, cell_size_y: int, win: Window):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._create_cells()

    def _create_cells(self):
        # create matrix of cells where `_num_col` are the num of `Cell` in the inner list and `_num_row` are the num of inner lists
        self._cells = [[Cell(self._win) for _ in range(self._num_cols)] for _ in range(self._num_rows)]

        # run the `_draw_cells` method for each cell in the matrix (with respect to the (i, j) position in the matrix)
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        # calculate the position of the top left cell point relative to the initial maze potition offest and the size of the cells
        x1 = (j * self._cell_size_x) + self._x1  # j is the number of cols, which is x
        y1 = (i * self._cell_size_y) + self._y1  # i is the number of rows, which is y

        # calculate the position of the bottom right cell point relative to x1 and y1
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y

        # draw the cell and animate the each object creation on the window canvas
        cell: Cell = self._cells[i][j]
        cell.draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.03)
