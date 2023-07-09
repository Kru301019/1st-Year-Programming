# Practical Worksheet P3: Graphical Programming
# your name, your number

from ctypes.wintypes import POINT
from graphics import *


def drawStickFigure():
    win = GraphWin("Stick figure",400,400)
    head = Circle(Point(200, 200), 20)
    head.draw(win)
    body = Line(Point(200, 220), Point(200, 300))
    body.draw(win)
    arm = Line(Point(150,250),Point(250,250))
    arm.draw(win)

    rightleg = Line(Point(200,300),Point(230,350))
    rightleg.draw(win)
    leftleg = Line(Point(200,300),Point(170,350))
    leftleg.draw(win)

drawStickFigure()

def drawLine():
    win = GraphWin("Line drawer")
    message = Text(Point(100,100), "Click on first point")
    message.draw(win)
    p1 = win.getMouse()
    message.setText("Click on second point")
    p2 = win.getMouse()
    line = Line(p1, p2)
    line.draw(win)
    message.setText("")
    win.getMouse()
drawLine()