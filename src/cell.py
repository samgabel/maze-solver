from graphics import Window, Point, Line


class Cell:
    def __init__(self, win: Window | None):
        """
        An object meant make up the structure of the maze grid (formed into a matrix of Cell objects)

        Parameters:
        `win` : the window object, or optionally set `win=None` for testing
        """

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
        """
        Draw the cell onto the Window object

        Parameters:
        `x1` , `y1`: the top left coordinate point on the window for the desired cell to be drawn
        `x2` , `y2`: the bottom right coordinate point on the window for the desired cell to be drawn
        """

        # don't continue to render ui when win=None (for testing purposes)
        if self._win is None:
            return

        # set cooridinate instance variables only when `draw` method is called
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        # draw cell walls based on instance variables `self.has_*`
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

    def draw_move(self, to_cell: 'Cell', undo=False):
        """
        Draw a line between the middle of 2 cells, the line is red if undo=False

        Parameters:
        `to_cell`: the other cell object that you want to draw a line to
        `undo`: a representation of the undo state based on color
        """

        # don't continue to render ui when win=None (for testing purposes)
        if self._win is None:
            return

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
