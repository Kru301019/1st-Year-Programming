from ctypes.wintypes import POINT
from re import X
from time import sleep
from tkinter import Y
from graphics import*

win = GraphWin()


for i in range(100):
 
 mouseClick = win.getMouse()

 x = mouseClick.getX()
 y = mouseClick.getY()

 C = Circle(Point(x,y),50)

 C.setFill('blue')
 C.draw(win)
 sleep(.02)

win.getMouse()


