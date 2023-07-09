# -------------------------------------------------------------------------------
# Practical Worksheet 7: Booleans and while loops
# your name, your number
# -------------------------------------------------------------------------------


from graphics import *
import time


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
    win = GraphWin("Traffic Lights", 200, 250)

    red = Circle(Point(100, 50), 20)
    red.setFill("red")
    red.draw(win)

    amber = Circle(Point(100, 100), 20)
    amber.setFill("black")
    amber.draw(win)

    green = Circle(Point(100, 150), 20)
    green.setFill("black")
    green.draw(win)

    while True:
        # Change lights to red
        red.setFill("red")
        amber.setFill("black")
        green.setFill("black")
        time.sleep(5)  # Delay for 5 seconds

        # Change lights to red/amber
        red.setFill("red")
        amber.setFill("yellow")
        green.setFill("black")
        time.sleep(2)  # Delay for 2 seconds

        # Change lights to green
        red.setFill("black")
        amber.setFill("black")
        green.setFill("green")
        time.sleep(5)  # Delay for 5 seconds

        # Change lights to amber
        red.setFill("black")
        amber.setFill("yellow")
        green.setFill("black")
        time.sleep(2)  # Delay for 2 seconds

    win.close()


trafficLights()

# For exercise 6


def fahrenheit2Celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def celsius2Fahrenheit(celsius):
    return 9 / 5 * celsius + 32
