from ftplib import parse150
from turtle import left, right
from pyparsing import line
from graphics import*


win = GraphWin('window',600,600)
                 #right,down
top_left = Point(30,100)
top_right = Point(570,100)
bottom_right = Point(570,490)
bottom_left = Point(30,490)


l1=Line(top_left, top_right)
l2=Line(top_right, bottom_right)
l3=Line(bottom_right, bottom_left)
l4=Line(bottom_left,top_left)

l1.draw(win)
l2.draw(win)
l3.draw(win)
l4.draw(win)

win.getMouse()
