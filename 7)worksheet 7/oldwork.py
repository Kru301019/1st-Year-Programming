from graphics import *
import math


def areaOfCircle(radius):
    return math.pi * radius ** 2


radius = 6
area = areaOfCircle(radius)


def circumferenceOfCircle(radius):
    return 2 * math.pi * radius


circumference = circumferenceOfCircle(radius)


def circleInfo(area, circumference):

    print(
        f'The area is {area:.3f} and the circumference is {circumference:.3f}')


def drawCircle(win, centre, radius, colour):
    circle = Circle(centre, radius)
    circle.setFill(colour)
    circle.setWidth(2)
    circle.draw(win)
    


def drawBrownEyeInCentre(x, y, win):

    
    centre = Point(x+50, y+50)
    radius = [50, 30, 15]
    colour = ['white', 'brown', 'black']

    for i in range(len(radius)):
        drawCircle(win, centre, radius[i], colour[i])

    


def drawBrownEye(win, centre, radius):

    colors = ['white', 'brown', 'black']
    for i in range(len(colors)):
        drawCircle(win, centre, radius, colors[i])
        radius /= 2

    win.getMouse()

def drawPairOfBrownEyes():

    win = GraphWin('', 400, 400)

    x = 100
    radius = 60

    for _ in range(2):

        drawBrownEye(win, Point(x, 100), radius)
        x += radius * 2

    win.getMouse()


def distanceBetweenPoints(p1, p2):
    return math.sqrt((p1.getX() - p2.getX())**2 + (p1.getY() - p2.getY())**2)


# print(distanceBetweenPoints(Point(1, 2), Point(4, 6)))

def drawBlocks(spaceOne, asterisksOne, spaceTwo, asterisksTwo, height):

    asterisksOne *= '*'
    asterisksTwo *= '*'

    for i in range(height):

        output = ' '*spaceOne + asterisksOne + ' '*spaceTwo + asterisksTwo

        print(output)


def drawLetterA():

    toDraw = [[2, 8, 0, 0, 2], [0, 2, 8, 2, 2],
              [0, 12, 0, 0, 2], [0, 2, 8, 2, 3]]

    for i in toDraw:
        drawBlocks(i[0], i[1], i[2], i[3], i[4])


def drawFourPairsOfBrownEyes():

    win = GraphWin("Beady eyes", 400, 400)
    for i in range(4):

        p1 = win.getMouse()
        p2 = win.getMouse()

        radius = distanceBetweenPoints(p1, p2)

        xLeft = p1.getX()
        xRight = xLeft + radius*2

        centreLeft = Point(xLeft, p1.getY())
        centreRight = Point(xRight, p1.getY())

        drawBrownEye(win, centreLeft, radius)
        drawBrownEye(win, centreRight, radius)

    win.close()


def displayTextWithSpaces(strings):

    output = ''

    for string in strings:
        output += string + ' '

    return output.upper()


def constructVisionChart():
    strings = []
    num_strings = int(input("Enter the number of strings: "))

    for i in range(num_strings):
        string = input("Enter a string: ")
        strings.append(string)

    lenthOfStrings = len(strings)

    winHeight = 100*lenthOfStrings
    winWidth = winHeight-50
    win = GraphWin('', winHeight, winWidth)
    y = 50
    textSize = 35
    for i in range(lenthOfStrings):
        center = Point(winHeight / 2, y)
        y += 50

        outputtext = displayTextWithSpaces(strings[i])
        text = Text(center, outputtext)

        text.setSize(textSize)
        text.draw(win)
        textSize -= 5

    win.getMouse()
    win.close()


# def drawStickFigure(win, x ,y):

#     head = Circle(Point(x, x-y), y)
#     head.draw(win)
#     body = Line(Point(x, x-y), Point(x, x+y))
#     body.draw(win)
#     leftLeg = Line(Point(x, x+y), Point(x-y, x+y*2))
#     leftLeg.draw(win)
#     rightLeg = Line(Point(x, x+y), Point(x+y, x+y*2))
#     rightLeg.draw(win)
#     leftArm = Line(Point(x, x), Point(x-y, x))
#     leftArm.draw(win)
#     rightArm = Line(Point(x, x), Point(x+y, x))
#     rightArm.draw(win)
#     win.getMouse()
    


# def drawStickFigureFamily():
#     win = GraphWin("Stick figure", 400, 400)
#     point = 100
#     size = 20
    
#     drawStickFigure(win, point ,size)
#     drawStickFigure(win, point+100, size+size)


#drawStickFigureFamily()

# def drawStickFigureFamilyTest():
#     win = GraphWin("Stick figure", 700, 500)
#     #drawStickFigure(Point(100,100), 5, win)
#     sticksToDraw = [[200, 300, 5], [250, 300, 4], [300, 300, 3], [325, 300, 2], [360, 300, 1]]
#     for currentStick in sticksToDraw:
#         drawStickFigure(Point(currentStick[0], currentStick[1]), currentStick[2], win)
   
#     win.getMouse()

# def drawStickFigureTest(centrePoint, mod, win):
#     centX = centrePoint.getX()
#     centY = centrePoint.getY()
#     neck = Point(centX, (centY-5*mod))
#     waist = Point(centX, (centY+10*mod))
#     body = Line(neck, waist)
#     body.draw(win)
#     headRad = 2*mod
#     head = Circle(Point(centX, neck.getY()-headRad), headRad)
#     head.draw(win)
#     arms = Line(Point((centX-3.5*mod), centY), Point((centX + 3.5*mod), centY))
#     arms.draw(win)
#     lleg = Line(waist, Point(waist.getX()-3*mod, waist.getY()+5*mod))
#     lleg.draw(win)
#     rleg = Line(waist, Point(waist.getX()+3*mod, waist.getY()+5*mod))
#     rleg.draw(win)

# drawStickFigureFamilyTest()