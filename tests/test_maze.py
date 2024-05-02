from src.maze import Maze


def test_maze_create_cells():
    num_cols = 12
    num_rows = 10
    m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win=None)
    assert len(m1._cells) == num_rows
    assert len(m1._cells[0]) == num_cols


def test_maze_create_cells_large():
    num_cols = 24
    num_rows = 36
    m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win=None)
    assert len(m1._cells) == num_rows
    assert len(m1._cells[0]) == num_cols
