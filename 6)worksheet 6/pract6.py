# Practical Worksheet 6: if statements and for loops
# your name, your number
from graphics import *
import math
import random


def fastFoodOrderPrice():
    order_total = float(input('Enter your order total: '))
    delivery_charge = 1.50

    if order_total >= 10:
        order_total += delivery_charge

    print('The total price of your order is:', order_total)


def whatToDoToday():
    temperature = float(input("Enter today's temperature: "))

    if temperature > 25:
        print('swim is good idea')

    elif 10 <= temperature <= 25:
        print('shopping in Gunwharf Quays is a good idea')

    else:
        print('it’s best to watch a film at home.')


def displaySquareRoots(start, end):
    for i in range(start, end + 1):
        print("The square root of {0:2} is {1:0.3f}".format(i, math.sqrt(i)))


def calculateGrade(score):
    if 16 <= score <= 20:
        return "A"
    elif 12 <= score <= 15:
        return "B"
    elif 8 <= score <= 11:
        return "C"
    elif 0 <= score <= 7:
        return "F"
    else:
        return "X"


def ticketPrice(distance, custAge):
    ticketBase = 3
    ticketPerKilo = .15
    ticketBaseTotal = ticketPerKilo * distance+ticketBase

    if custAge >= 60 or custAge <= 15:
        discount = ticketBaseTotal * .40

        discountedTicket = ticketBaseTotal-discount
        return discountedTicket
    return ticketBaseTotal


distance = 100
age = 55
printPrice = ticketPrice(distance, age)


def numberedSquare(n):

    for i in range(n, 0, -1):
        for j in range(n):

            print(i, end='  ')
            i += j

        print('')


def drawCircle(win, centre, radius, colour):
    circle = Circle(centre, radius)
    circle.setFill(colour)
    circle.setWidth(2)
    circle.draw(win)


def drawColouredEye(win, centre, radius, colour):

    colours = ['white', colour, 'black']
    for eyeColor in colours:
        drawCircle(win, centre, radius, eyeColor)
        radius -= radius/2


def eyePicker():

    x = eval(input("Enter x: "))
    y = eval(input("Enter y: "))

    radius = int(input('Enter radius: '))
    colour = input('Enter colour: ')
    if (colour == 'brown' or 'blue' or 'grey' or 'green'):
        win = GraphWin('', 400, 400)
        drawColouredEye(win, Point(x, y), radius, colour)

    else:
        print('not valid eye color')


def drawPatchWindow():
    steps = 15
    h = steps**2
    w = steps**2
    win = GraphWin('Patchwork Window', h, w)

    for x in range(0, h+1, steps):
        lineLeft = Line(Point(0, x), Point(x, h))
        lineLeft.draw(win)

        lineRight = Line(Point(x, 0), Point(w, x))
        lineRight.draw(win)

    win.getMouse()
    win.close()


def drawPatch(win, xCord, yCord):
    x = 0

    for i in range(11):
        lineLeft = Line(Point(0+xCord, x+yCord), Point(x+xCord, 100+yCord))
        lineLeft.draw(win)

        lineRight = Line(Point(x+xCord, 0+yCord), Point(100+xCord, x+yCord))
        lineRight.draw(win)
        x += 10


def drawPatchwork():

    win = GraphWin('Patchwork Window', 500, 700)

    patchSize = 100

    for i in range(2):
        for j in range(3):
            xCord = j * patchSize
            yCord = i * patchSize
            drawPatch(win, xCord, yCord)

    win.getMouse()
    win.close()


def eyesAllAround():
    win = GraphWin('', 500, 500)
    radius = 30

    colours = ['blue', 'grey', 'green', 'brown']
    colcount = 0

    for i in range(0, 30, 1):

        drawColouredEye(win, win.getMouse(), radius, colours[colcount])

        colcount = (colcount + 1) % 4
    win.close()


def distanceBetweenPoints(p1, p2):
    return math.sqrt(((p2.getX()-p1.getX())**2) + (p2.getY()-p1.getY())**2)


def archeryGame():
    h = 300
    w = 300
    adjustSize = h/6
    win = GraphWin('', h, w)
    centre = Point(h/2, w/2)
    radius = [h/4, adjustSize, h/12]

    colors = ['blue', 'red', 'yellow']
    for i in range(len(colors)):
        drawCircle(win, centre, radius[i], colors[i])

    point = 0
    for _ in range(5):

        getMouseClick = win.getMouse()
        x = getMouseClick.getX() + random.randint(1, 3)
        y = getMouseClick.getY() + random.randint(1, 3)
        cen = Point(x, y)

        drawCircle(win, cen, 5, 'black')
        distance = distanceBetweenPoints(cen, centre)

        if distance <= radius[2]:

            point += 10
        elif radius[2] < distance <= radius[1]:

            point += 5
        elif radius[1] < distance <= radius[0]:

            point += 2
        else:
            print('you missed it by long shot')

    finalScore = Text(Point(h/2, adjustSize), "Final Score: " + str(point))
    finalScore.setSize(15)
    finalScore.draw(win)
    win.getMouse()
    win.close()


archeryGame()
