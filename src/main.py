from graphics import Window
from cell import Cell


def main():
    win = Window(800, 600)

    # top left box
    l1 = Cell(win)
    l1.draw(280, 150, 330, 200)

    # top right box
    r1 = Cell(win)
    r1.draw(470, 150, 520, 200)

    # bottom left box
    l2 = Cell(win)
    l2.draw(280, 350, 330, 400)

    # bottom right box
    r2 = Cell(win)
    r2.draw(470, 350, 520, 400)

    # draw lines between cells
    l1.draw_move(r1, undo=False)
    r1.draw_move(r2, undo=False)
    l2.draw_move(l1, undo=False)
    l1.draw_move(r2, undo=True)

    win.wait_for_close()

main()
