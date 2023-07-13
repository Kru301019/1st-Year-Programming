# -------------------------------------------------------------------------------
# Practical Worksheet 7: Booleans and while loops
# your name, your number
# -------------------------------------------------------------------------------


# from graphics import *
import time
from graphics import *
from oldwork import distanceBetweenPoints, drawBrownEye, drawBrownEyeInCentre
import random


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
    txt = ''
    t = Text(Point(100, 225), txt)
    t.draw(win)
    while True:
        userClick = win.getMouse()
        distance = distanceBetweenPoints(eyeCenter, userClick)

        if distance <= 25:
            txt = 'pupil'
        elif 25 < distance <= 50:
            txt = 'iris'
        elif 50 < distance <= 100:
            txt = 'eyeball'
        else:
            break
        t.setText(txt)
    win.getMouse()
    win.close()

# For exercise 6


def fahrenheit2Celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def celsius2Fahrenheit(celsius):
    return 9 / 5 * celsius + 32


def temperatureConverter():
    while True:
        convertTo = input(
            "Type 'F2C' to convert Fahrenheit to Celsius or 'C2F' to convert Celsius to Fahrenheit, or 'STOP' to stop: ")

        if convertTo == 'F2C':
            fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
            celsius = fahrenheit2Celsius(fahrenheit)
            print(f"{fahrenheit}°F is equivalent to {celsius:.2f}°C")

        elif convertTo == 'C2F':
            celsius = float(input("Enter the temperature in Celsius: "))
            fahrenheit = celsius2Fahrenheit(celsius)
            print(f"{celsius}°C is equivalent to {fahrenheit:.2f}°F")

        elif convertTo == 'STOP':
            break

        else:
            print("Please enter a valid option.")


def randomGen(start, end):
    return random.randint(start, end)


def guessTheNumber():
    ranNum = randomGen(1, 100)

    count = 0
    while count <= 6:
        guessNum = int(input('Enter number to guess: '))
        diffrence = guessNum-ranNum
        print('diffrence=', diffrence)

        if diffrence == 0:
            print('match')
            break
        elif diffrence > 20 or diffrence < -20:
            print('too high')

        elif diffrence < 20 or diffrence > -20:
            print('close')

        print('random=', ranNum)

        count += 1


def tableTennisScorer():
    win = GraphWin("Table Tennis Scorer", 400, 200)

    playerAScore = 0
    playerBScore = 0

    playerAText = Text(Point(100, 100), str(playerAScore))
    playerAText.draw(win)

    playerBText = Text(Point(300, 100), str(playerBScore))
    playerBText.draw(win)

    while True:
        click = win.getMouse()
        clickX = click.getX()

        if clickX < 200:
            playerAScore += 1
            playerAText.setText(str(playerAScore))
        else:
            playerBScore += 1
            playerBText.setText(str(playerBScore))

        if playerAScore >= 11 and playerAScore >= playerBScore + 2:
            winnerText = Text(Point(100, 50), "A wins!")
            winnerText.draw(win)
            break

        if playerBScore >= 11 and playerBScore >= playerAScore + 2:
            winnerText = Text(Point(300, 50), "B wins!")
            winnerText.draw(win)
            break

    win.getMouse()
    win.close()


def clickableBoxOfEyes(column, row):
    h = column + 1  # 500
    w = row + 1  # 300
    height = 100*h
    width = 100*w
    win = GraphWin('', height, width)

    a = 0
    b = 90

    box = Rectangle(Point(a, b), Point(column*100+a, row*100+b))
    box.draw(win)

    for x in range(0+a, column*100+a, 100):

        for y in range(0+b, row*100+b, 100):
            drawBrownEyeInCentre(x, y, win)

    while 0 < 100:
        MouseClick = win.getMouse()
        clickCircle = Circle(Point(MouseClick.getX(), MouseClick.getY()), 5)
        clickCircle.draw(win)
        clickCircle.setFill('black')

    win.getMouse()


def findTheCircle():
    chance = 0
    newRad=0
    dox = True
    while dox:
        win = GraphWin('', 400, 400)

        x = randomGen(30, 370)
        y = randomGen(30, 370)

        while chance < 10:

            userClick = win.getMouse()
            userX = userClick.getX()
            userY = userClick.getY()
            distance = distanceBetweenPoints(Point(userX, userY), Point(x, y))
          
            radius =30-newRad
            circle = Circle(Point(x, y), radius)
            
            chance += 1
            
            if distance <= radius:
                circle.draw(win)
                print('Congratulations you found the cirlce and your Point is: ', chance)
                chance=0
                calRad = radius*0.1 
                newRad += calRad
                win.close()
                break

            elif radius < distance < 100:
                print('Getting closer')

            else:
                print('Getting furthur away')

            if chance == 10:
                print('Fail')
                dox = False
                
        
    win.getMouse()


findTheCircle()
