from graphics import *
import math

def makeDictionary():

    words = []
    while True:
        word = input("Enter word (ret to exit): ")
        if word == "":
            break
        words.append(word)
    words.sort()
    for word in words:
        print(word)

def displayDate(day, month, year):

    months = ['january', 'february', 'march', 'april', 'may', 'june',
              'july', 'august', 'september', 'october', 'november', 'december']
    print('{} {} {}'.format(day, months[month-1], year))

# displayDate(14,3,2019)

def wordLengths():
    fruits = ["bacon", "jam", "spam"]
    
    for i in range(3):
        count = 0
        for _ in fruits[i]:
           
            count+=1
        print('{} {}'.format(fruits[i], count))
      
def wordLengthsCopy():
    fruits = ["bacon", "jam", "spam"]

    for fruit in fruits:
        count = len(fruit)
        print('{} {}'.format(fruit, count))

def draw_polygon():
    # Create a graphics window
    win = GraphWin("Polygon", 400, 400)

    # Define the vertices of the polygon
    vertices = [
        Point(150, 50),
        Point(250, 150),
        Point(250, 250),
        Point(150, 350),
        Point(50, 250),
        Point(50, 150)
    ]

    # Create the polygon shape
    polygon = Polygon(vertices)
    polygon.setFill("lightblue")
    polygon.setOutline("black")
    polygon.setWidth(2)

    # Draw the polygon in the window
    polygon.draw(win)

    # Wait for a mouse click to close the window
    win.getMouse()
    win.close()

# Call the function to draw the polygon
def testMarks():
    marks = [4, 0, 4, 1, 1, 4, 3 ,5]
    for i in range(6):
        print('{} student(s) got {} makrs'.format(marks.count(i),i))

def drawBarChart():
    str = [3, 1, 2]
    line=''
    for i in range(3):
        line += "  "
        for i in str:
            line='#'
        
        print(line)

def distanceBetweenPoints(x ,y):
    x1, y1 = x
    x2, y2 = y
    return math.sqrt((x1 - x2)**2 + (y1 -y2)**2)

#print(distanceBetweenPoints((1, 2), (4, 6)))

def countCharacters():
    user_input = input("Enter a string: ")
    char_count = {}
   
    for char in user_input:
         if char in char_count:
             char_count[char] += 1
         else:
             char_count[char] = 1

    for char, count in char_count.items():
         print(f"{count} occurrences of '{char}'")




