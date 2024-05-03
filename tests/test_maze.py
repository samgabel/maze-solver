from maze import Maze


def test_maze_create_cells():
    num_cols = 12
    num_rows = 10
    m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win=None)
    assert len(m1._cells) == num_rows
    assert len(m1._cells[0]) == num_cols


def test_maze_break_entrance_and_exit():
    num_cols = 12
    num_rows = 10
    m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win=None)
    assert m1._cells[0][0].has_top_wall == False
    assert m1._cells[-1][-1].has_bottom_wall == False

def test_maze_reset_cells_visited():
    num_cols = 12
    num_rows = 10
    m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win=None)
    for row in m1._cells:
        for cell in row:
            assert cell.visited == False

def test_maze_solve():
    num_cols = 12
    num_rows = 10
    m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win=None, seed=0)
    assert m1.solve() == True
