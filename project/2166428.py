from graphics import*

#student name = Krutarth Joshi 
#student ID = UP2166428 

def bR(tL):
    x = tL.getX() + 100
    y = tL.getY() + 100
    bR = Point(x, y)
    return bR

def centre(tL, radius):
    x = tL.getX() + radius
    y = tL.getY() + radius
    centre = Point(x, y)
    return centre

def drawcircle(win,centre,radius,colour,colorForF):
    
    circlE = Circle(centre,radius)
    circlE.setOutline(colorForF)
    circlE.setFill(colour)
    circlE.draw(win)

def drawcirclefromtL(win, x, y, radius, colour, colorForF):
    add = 0
    for i in range(2):
        centre = Point(x+5+add, y+5)
        centre2 = Point(x+5+add, y+15)

        circlE = Circle(centre, radius)
        circlE2 = Circle(centre2, radius)
        circlE.setOutline(colorForF)
        circlE.setFill(colour)
        circlE2.setFill(colour)

        circlE.draw(win)
        circlE2.draw(win)
        add += 10

def drawrectangle(win,tL,bR,colour): 
    
    rectanglE = Rectangle(tL,bR)
    rectanglE.setFill(colour)
    rectanglE.draw(win)
       
def drawF(win, x, y, screensizE, radius, noth, colorForF, counter):
    
    for i in range(11):
        tL = Point(x,y)
        x+=5
        y+=10
        radius-=5
        
        if counter == 1:
                drawcircle(win, centre(tL, radius), radius, '', colorForF[0])
          
        elif screensizE == 500 and counter == 5:
                drawcircle(win, centre(tL, radius), radius, '', colorForF[0])
        
        elif screensizE == 700 and counter == 7:
                drawcircle(win, centre(tL, radius), radius, '', colorForF[0])
        
        else:
                drawcircle(win, centre(tL, radius), radius, '', colorForF[2])
               
def drawP(win, x, y, screensizE, radius, colour, counter):
    
    yRange1 = [0, 200, 400, 600]
    yRange2=[100,300,500,700]
    
    dox=True
    for i in range(4):
        for x in range(0,screensizE,20): 
         for y in range(yRange1[i],yRange2[i],20):
             
            if x < 100 and y < 100 or 300 > x > 180 and 300 > y > 180 or 500 > x > 380 and 500 > y > 380 or 700 > x > 580 and 700 > y > 580:
                pass

            else:
                tL = Point(x,y)    
                brPoint = Point(x+20, y+20)
                
                if 380>=x>=100 and 380>=y>=100 and screensizE==500:
                    if dox==True:
                            drawrectangle(win,tL,brPoint,colour[3]) 
                            drawcirclefromtL(win,x,y,5,colour[2],'')                     
                    else:
                            drawrectangle(win,tL,brPoint,colour[2])  
                            drawcirclefromtL(win,x,y,5,colour[3],'')     
                    dox=not dox
                elif 580>=x>=100 and 580>=y>=100 and screensizE==700:
                        if dox==True:
                                drawrectangle(win,tL,brPoint,colour[3]) 
                                drawcirclefromtL(win,x,y,5,colour[2],'')                    
                        else:
                                drawrectangle(win,tL,brPoint,colour[2])  
                                drawcirclefromtL(win,x,y,5,colour[3],'')     
                        dox=not dox
                else:
                    if dox==True:
                            drawrectangle(win,tL,brPoint,colour[3]) 
                            drawcirclefromtL(win,x,y,5,colour[1],'')                    
                    else:
                            drawrectangle(win,tL,brPoint,colour[3])  
                            drawcirclefromtL(win,x,y,5,colour[0],'')
                    dox=not dox
                            
def plainpatcH(win, x2, y2, screensizE, colour, counter):
    counter2 = 0
    
    for i in range(3):    
        counter2+=1
        
        tL = Point(x2, y2)
        y2+=200
        
        if counter == 2 and counter2 == 1 or counter == 4 and counter2 == 2 or counter == 6 and counter2 == 3:
            pass
               
        elif  6>=counter>= 2 and counter2<=3 and screensizE==700: 
            drawrectangle(win, tL, bR(tL), colour[2])
            
        elif 4 >= counter >= 2 and counter2 <= 2 and screensizE == 500:
            drawrectangle(win, tL, bR(tL), colour[2])
            
        else:
            drawrectangle(win, tL, bR(tL), colour[1])
    
def main():
    print('valid size are 500*500 or 700*700')
    screensizE = int(input('Enter size of the window in single digit:'))*100
    
    print('valid colours are : (1)blue(2)orange(3)red(4)purple(5)cyan and (6)green')
    colour1=input('Enter colour one:')
    colour2=input('Enter colour two:')
    colour3=input('Enter colour two:')

    if colour1 and colour2 and colour3 =='blue' or colour1 and colour2 and colour3=='orange' or colour1 and colour2 and colour3=='red' or colour1 and colour2 and colour3=='purple' or colour1 and colour2 and colour3=='cyan' or colour1 and colour2 and colour3=='green':
      colour=[colour1,colour2,colour3,'white']
    else:    
        print('invalid colour')
    
    radius = 55
    x=0
    y=0 
    rangE=0
    
    if screensizE==500:
        rangE+=5
    else:
        rangE+=7  
    
    x2=0
    y2=100
    x3=0
    y3=0

    win = GraphWin('patch',screensizE,screensizE)
     
    counter = 0
    drawP(win, x3, y3, screensizE, radius, colour, counter)
        
    for i in range(rangE):
            
        counter+=1
        
        drawF(win, x,y, screensizE, radius, '',colour,counter)
        x += 100
        y += 100
               
        plainpatcH(win, x2, y2, screensizE, colour, counter)
        x2+= 100    
        x3 += 100

    win.getMouse()
            
main()               
