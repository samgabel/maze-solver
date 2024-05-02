from graphics import Window
from cell import Cell


def main():
    win = Window(800, 600)

    # top left box
    c = Cell(win)
    c.draw(280, 50, 330, 100)

    # top right box
    c = Cell(win)
    c.draw(470, 50, 520, 100)

    # bottom box
    c = Cell(win)
    c.has_top_wall = False
    c.draw(280, 150, 520, 200)

    # surrounding box
    c = Cell(win)
    c.draw(250, 20, 550, 230)

    win.wait_for_close()

main()
