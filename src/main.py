from graphics import Window, Point, Line


def main():
    win = Window(800, 600)

    l1 = Line(Point(230, 50), Point(270, 50))
    win.draw_line(l1, "red")
    l2 = Line(Point(530, 50), Point(570, 50))
    win.draw_line(l2, "red")
    l3 = Line(Point(230, 150), Point(570, 150))
    win.draw_line(l3, "red")

    win.wait_for_close()


main()
