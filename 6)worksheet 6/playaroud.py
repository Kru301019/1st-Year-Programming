import math
from graphics import*

def moduleMark(test,coursework):
    return test+coursework

def main():

    test = int(input('Enter test mark :'))
    coursework = int(input('Enter coursework mark :'))

    module = moduleMark(test,coursework)

    if module >=40:   #== !=
        print('congratulations you pass with {} marks'.format(module))
    else:
        print('umm {} try harder next time!'.format(module))


    #print(module)

def ifelse():

    test = int(input('Enter test mark :'))
    coursework = int(input('Enter coursework mark :'))

    module = moduleMark(test,coursework)

    if module >=70:
        print('1ST',module)

    if module <=69 and module>=50:
        print('2nd',module)

    if module <= 49 and module >=30:
        print('3nd',module)

    if module<=29:
        print('fail',module)

def eelif():

     test = int(input('Enter test mark :'))
     coursework = int(input('Enter coursework mark :'))

     module = moduleMark(test,coursework)

     if module >100:
        print('error')

     elif module==100:
        print('award')

     elif module >=70:
         print('1ST',module)

     elif module >=60:
         print('2nd',module)

     elif module >= 50:
         print('3nd',module)

     else:
         print('fail',module)

def areaofCircle(radius):

    area = math.pi*radius**2
    return area

def costofcircle(radius):
    cmCost = 0.015
    area = areaofCircle(radius)
    return area *cmCost

def drawcircle(win,radius,centre,colour):

    cir = Circle(centre,radius)
    cir.setFill(colour)
    cir.draw(win)

def main():

    win = GraphWin("hello",500,500)

    colours = ["brown","red","yellow"]

    for i in range(3):
        centre = win.getMouse()
        index = 0
        for radius in range(100,40,-20):

            drawcircle(win,radius,centre,colours[index])
            index+=1
        #drawcircle(win,80,centre,colours[1])
        #drawcircle(win,40,centre,colours[2])

    win.getMouse()

def timetable():

    for i in range(4,0,-1):
        for j in range(1, 5,  1):

         print("{0:3}".format(i*j), end=" ")

        print('')
timetable()











