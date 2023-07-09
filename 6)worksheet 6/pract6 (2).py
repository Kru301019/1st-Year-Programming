# Practical Worksheet 6: if statements and for loops
# your name, your number


from graphics import *
import math

def fastFoodOrderPrice():
    
    orderPrice = int(input('Enter order basic price of an order:'))
    
    if orderPrice>10 :

        print('your delivery is free.total amout to be paid is:')

    if orderPrice<10 :

        deliveryCharge = 1.50
        orderPrice = orderPrice + deliveryCharge
        print("your order total incluing delivery is :",orderPrice)

         
    
def whatToDoToday():
    
    temp = int(input('Enter todays tempertature:'))
    if temp >= 25:
        print('go to swim')
    if temp <= 25 and temp >= 10:
        print('shopping in gunwrarf')
    if temp<10:
        print('watch a film')    
            

def displaySquareRoots():
    
    for i in range(2,5):
        
        root = math.sqrt(i)
        print('the square root of {} is {:.3f} '.format(i,root)) 

def calculateGrade():
    
    marK = int(input('Enter marks:'))
    
    if marK >= 16:
        print('A')
    elif marK >=12:
        print('B')
    elif marK >=8:
        print('C')
    else :
        print('F')            

def peasInAPod():
    
    circleNumb = int(input('how many ponds'))
    windowSize = 100*circleNumb
    win = GraphWin('hello',windowSize,100)
    x = 10*5
    radiUs = 50
    y = 50
    
    for i in range(circleNumb):
        
        cir = Circle(Point(x,y),radiUs)
        x+=100
        cir.setFill('green')
        cir.draw(win)
    
    win.getMouse()

   


def ticketPrice(passangerAge,Distance):
    
    if passangerAge>=60 or passangerAge<=15:
        
        cal = 3.15*40
        perPrice= cal/100
        price = Distance*perPrice
        print('The passanger needs to pay {.2f}'.format(price))

    else:
        
        price = Distance*3.15
        print(price)        

def tarvelinfo():
    
    passangerAge = int(input('Enter age:') )
    Distance = int(input('Enter distance:'))
    ticketPrice(passangerAge,Distance)
       
def numberedSquare():

    number = int(input('Enter number'))    
    for i in range(number,0,-1):
          
        print("")
          
        for j in range(4):
          
            print("{0:2}".format(i), end=" ")
            i+=1

# For exercises 8 & 11


# For exercise 8

 
    
    
    


def drawPatchWindow():
    
    win = GraphWin('',200,200)
    
    x1=0
    y1=0
    x2=20
    y2=200
    
    xx1=0
    yy1=0
    
    xx2=200
    yy2=20
    
    for i in range(10):
        
       
       
        lineLeft = Line(Point(x1,y1),Point(x2,y2)) 
        
        lineRight = Line(Point(xx1,yy1),Point(xx2,yy2))
        
        y1+=20
        x2+=20
        
        yy2+=20
        xx1+=20
        
        lineRight.setFill('red')
        lineRight.draw(win)  
        
        lineLeft.setFill('red')
        lineLeft.draw(win)   
                                      
drawPatchWindow()  
def drawPatchWindow2():
    
    win = GraphWin('',200,200)
    
    
    y1 = 0
    x2 = 200
    x1=0
    y2=200
    
    yy1 = 0
    xx2 = 0
    xxx2 = 0
    yyy1 = 0
      
    for i in range(10):
        
      lineLeft = Line(Point(0,y1),Point(x2,200)) 
      
      x2 = x2-20 
      y1 = y1+20

      lineLeft.setFill('red')
      lineLeft.draw(win)
    
      lineright = Line(Point(x1,0),Point(200,y2)) 
      
      x1 = x1+20
      y2 = y2-20
      
      lineright.setFill('red')
      lineright.draw(win)
          
      linedown = Line(Point(200,yy1), Point(xx2,200))
      yy1 = yy1+20
      xx2 = xx2+20
        
      linedown.setFill('red')
      linedown.draw(win)
        
       
      lineup = Line(Point(0,yyy1), Point(xxx2,0))
      yyy1 = yyy1+20
      xxx2 = xxx2+20
        
      lineup.setFill('red')
      lineup.draw(win)


def drawPatchWindow5():
    
    win = GraphWin('',200,200)
    y1 = 40 
    x1 = 40
    x=20
    x2=20
    x3=20
    x4=20
    x5=20
    for i in range(5):
        
        Hline = Line(Point(0,y1) ,Point(200,y1))
        y1+=40
        
        Hline.draw(win)
        
        Vline = Line(Point(x1,0) ,Point(x1,200))
        x1+=40
        
        Vline.draw(win)
       
        y = 20
        
        text = Text(Point(x,y),'hi!')
        x+=40
        text.setFill('red')
        text.draw(win)
        
        text2 = Text(Point(x2,y+40),'hi!')
        x2+=40
        text2.setFill('red')
        text2.draw(win)
        
        text3 = Text(Point(x3,y+80),'hi!')
        x3+=40
        text3.setFill('red')
        text3.draw(win)
        
        text4 = Text(Point(x4,y+120),'hi!')
        x4+=40
        text4.setFill('red')
        text4.draw(win)
        
        text5 = Text(Point(x5,y+160),'hi!')
        x5+=40
        text5.setFill('red')
        text5.draw(win)




def drawPatchWindow8():
    
    win = GraphWin('',200,200)
    
    radius = 5
    y = 195
   
    for i in range(10):
   
    
     cir = Circle(Point(100,y), radius )
     y = y-5
     radius+=5
     
     cir.setOutline('red')
     cir.draw(win)
 
def drawPatchWindow6():
    
    win = GraphWin('',200,200) 
    x = 20
    y = 20 
    for i in range(5):
    
      cir = Circle(Point(x,20), 20)
      x+=40
      cir.setFill('red')
      cir.setOutline('red')
      cir.draw(win) 
     
      cir = Circle(Point(x-40,60) ,20) 
      cir.setOutline('red')
      cir.draw(win)  
      
      cir = Circle(Point(x-40,100) ,20) 
      cir.setFill('red')
      cir.setOutline('red')
      cir.draw(win) 
      
      cir = Circle(Point(x-40,140) ,20) 
      
      cir.setOutline('red')
      cir.draw(win)
      
      cir = Circle(Point(x-40,180) ,20) 
      cir.setFill('red')
      cir.setOutline('red')
      cir.draw(win) 

def drawPatchWindow9():
    
    win = GraphWin('',200,200)
    
    y = 0
    y2 = 200
    x1 = 0
    x2 = 200
    for i in range(11):
        
        line = Line(Point(0,y), Point(200,y2))
        y+=20
        y2=y2-20
        line.setOutline('red')
        line.draw(win) 
        
        lineUp = Line(Point(x1,0), Point(x2,200))
        x1+=20
        x2=x2-20
        
        lineUp.setOutline('red')
        lineUp.draw(win)
    
def drawCircle(win, centre, radius, colour):
    
    circle = Circle(centre, radius)
    circle.setFill(colour) 
    circle.setWidth(2)
    circle.draw(win)

def drawColouredEye():
    
    win = GraphWin('hello',400,400)
    
    win = win.getMouse()
    
    for i in range(10):
       x1 = win.getX()
       y1 = win.getY()
       centre = Point(x1,y1)
       radius1 = 60
       radius2 = 40
       radius3 = 20
    
       colour1= 'white'
       colour2 = 'grey'#input('Enter Eye colour:')
       colour3 = 'black'
   
       drawCircle(win,centre,radius1,colour1)
    
       if colour2=='brown' or colour2=="blue" or colour2=="green" or        colour2=='grey': 
    
        drawCircle(win,centre,radius2,colour2)
    
       else:
    
        print('error')
    
        drawCircle(win,centre,radius3,colour3)

def Drawpatch7():

    win = GraphWin('win',200,200)
 
    x1 = 80
    y1 = 80
    x2 = 120
    y2 = 120 
    width = 10
    for i  in range(5): 
        
        rect = Rectangle(Point(x1,y1),Point(x2,y2))
        
        x1=x1-20
        y1=y1-20
        
        x2+=20
        y2+=20
        
        rect.setWidth(width)
        rect.setOutline('red')

        rect.draw(win)

def twonumbers():
    
    num1,num2 = input('Enter numbers:')
    
    print('numbers are',num1+num2)


def drawPatch(win,colour,tL,bR,width):

    rect = Rectangle(tL,bR)
    rect.setOutline(colour)
    rect.setWidth(width)
    rect.draw(win)
    win.getMouse()

def patchwork():

    win = GraphWin('',300,200)
    win.getMouse()
    
   
   
   
    for y in range(0,200,100):        
       
        for x in range(0,300,100):   
          
         for i in range(5):
           
           colour = 'blue'
           tL=Point(x,y)
           bR=Point(100-tL.x,100-tL.y)
           width = 5
           drawPatch(win,colour,tL,bR,width)
           x+=10   
           y+=10
           
         
patchwork()    
    
    
     











































   
    
    
