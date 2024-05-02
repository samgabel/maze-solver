from graphics import Window, Point, Line


class Cell:
    def __init__(self, win: Window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1: int
        self._y1: int
        self._x2: int
        self._y2: int
        self._win = win

    def draw(self, x1: int, y1: int, x2: int, y2: int):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        if self.has_left_wall == True:
            l = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(l, "black")
        if self.has_right_wall == True:
            l = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(l, "black")
        if self.has_top_wall == True:
            l = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(l, "black")
        if self.has_bottom_wall == True:
            l = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(l, "black")

    def draw_move(self, to_cell, undo=False):
        """
        Draw a line between the middle of 2 cells, the line is red if undo=False
        """
        # error handling for cases where a cell object is not properly instantiated
        if (self._y1 == None and self._y2 == None and to_cell._y1 == None and to_cell._y2 == None):
            raise ValueError("Need to instantiate cell points with Cell method `draw`")

        # find the center of the cell for `self`
        center_x1 = self._x1 + (abs(self._x1 - self._x2) // 2)
        center_y1 = self._y1 + (abs(self._y1 - self._y2) // 2)

        # find the center of the cell for `to_cell`
        center_x2 = to_cell._x1 + (abs(to_cell._x1 - to_cell._x2) // 2)
        center_y2 = to_cell._y1 + (abs(to_cell._y1 - to_cell._y2) // 2)

        # provide color marker for undo status
        if undo == False:
            fill_color = "red"
        else:
            fill_color = "grey"

        # draw line between cells
        l = Line(Point(center_x1, center_y1), Point(center_x2, center_y2))
        self._win.draw_line(l, fill_color)
