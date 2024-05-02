from graphics import Window, Point, Line


class Cell:
    def __init__(self, win: Window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2):
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
