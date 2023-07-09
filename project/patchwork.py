from graphics import *


def drawcircle(win, centre, radius, color):

    circlE = Circle(centre, radius)
    circlE.setOutline(color)
#    circlE.setFill(color)
    circlE.draw(win)


def patchOne(win, x, y, radOne, color):

    for i in range(10):
        drawcircle(win, Point(x, y), radOne, color)
        radOne += 5
        y -= 5


def main():

    winSize = 5
    win = GraphWin('', 500, 500)
    radOne = 5

    x, y = 50, 95
    for i in range(winSize):
        if i == winSize-1 or i == 0:
            patchOne(win, x, y, radOne, 'red')

        else:
            patchOne(win, x, y, radOne, 'black')
        x += 100
        y += 100
    win.getMouse()


main()
