# -------------------------------------------------------------------------------
# Practical Worksheet 7: Booleans and while loops
# your name, your number
# -------------------------------------------------------------------------------


# from graphics import *
import time
from graphics import *
from oldwork import distanceBetweenPoints, drawBrownEye


def getName():
    dox = True
    while dox:
        enterName = input('Enter Name: ')
        if enterName.isalpha():
            print('name: ', enterName)
            dox = not dox
        else:
            dox


# For exercise 2

def trafficLights():
    black = color_rgb(0, 0, 0)
    white = color_rgb(255, 255, 255)
    red = color_rgb(255, 0, 0)
    amber = color_rgb(255, 194, 0)
    green = color_rgb(26, 173, 12)

    win = GraphWin("TL", 100, 300)
    win.setBackground(black)
    r = Circle(Point(50, 50), 50)
    r.draw(win)
    r.setFill(black)
    r.setOutline(white)
    a = Circle(Point(50, 150), 50)
    a.draw(win)
    a.setFill(black)
    a.setOutline(white)
    g = Circle(Point(50, 250), 50)
    g.draw(win)
    g.setFill(black)
    g.setOutline(white)

    while True:
        r.setFill(red)
        time.sleep(5)
        a.setFill(amber)
        time.sleep(5)
        r.setFill(black)
        a.setFill(black)
        g.setFill(green)
        time.sleep(2)
        g.setFill(black)
        a.setFill(amber)
        time.sleep(5)
        a.setFill(black)


def calculateGrade(score):
    if (score >= 16 and score <= 20):
        return ("A")
    elif (score >= 12 and score <= 15):
        return ("B")
    elif (score >= 8 and score <= 11):
        return ("C")
    elif (score >= 0 and score <= 7):
        return ("F")
    else:
        return ("X")


def gradeCoursework():
    mark = int(input('Enter your mark '))
    while mark > 20:
        mark = int(input('Enter your mark '))

    print(calculateGrade(mark))


def orderPrice():
    total = 0

    while True:
        choclatePrice = int(input('Enter product price: '))
        howMany = int(input('Enter product quantity: '))
        moreProduct = input('Do you need more product? (yes or no): ')

        total += choclatePrice * howMany

        if moreProduct.lower() == 'no':
            break

    print("The total price is £{0:0.2f}".format(total))


def clickableEye():
    win = GraphWin("Window", 500, 500)
    eyeCenter = Point(250, 250)
    eyeRadius = 100

    drawBrownEye(win, eyeCenter, eyeRadius)

    while True:
        userClick = win.getMouse()
        distance = distanceBetweenPoints(eyeCenter, userClick)
        
        if distance <= 25:
            print('Black')
        elif 25 < distance <= 50:
            print('Brown')
        elif 50 < distance <= 100:
            print('White')
        else:
            break

    win.getMouse()
    win.close()


clickableEye()

# For exercise 6


def fahrenheit2Celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def celsius2Fahrenheit(celsius):
    return 9 / 5 * celsius + 32
