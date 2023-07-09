from graphics import*

win = GraphWin()

for i in range(10):

 x = win.getMouse()
 y= win.getMouse() 



 l = Line(x,y)

 l.draw(win)


win.getMouse()