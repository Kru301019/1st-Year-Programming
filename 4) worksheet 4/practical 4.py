from time import sleep

from string import*

def personalGreeting(): 

 s1 = 'hello'+" "

 s2 = (input('Enter your name-:'))

 s3 = 'nice to see you!' 
 s=s1+s2+','+s3
 print(' is :',s)
 
 
def formalName():
    
  s1 = input('Enter your first name:',)

  s2 = input('Enter your second name:')

  print('your name:',s1[0].upper()+" "+s2.capitalize())
  
def kilos2pounds():  
  
  kilos = int(input('Enter weights in kgs'))
  pounds = 2*kilos

  print('weight in {:0.2f} and {} is:'.format(kilos,pounds))
  
  #x = 10.123
  #y = 20
  #print('values are {:0.3f} and {1:2}'.format(x,y))
 
def generateEmail():
    
    First_name = input('Enter your First name:')
    second_name = input('Enter your second name:')
    year = input('Enter year you are studying:') 
    student_email = second_name+'.'+First_name[0].capitalize()+year[2:4]+'.@myport.ac.uk'

    print('your email is :',student_email)
    
def gradeTest():
    
   mark = int(input("Please Enter marks "))
   grade = "FFFFCCBBAAA"

   userMark = grade[mark]    
    
   print("You have selected :",userMark) 
                 
def graphicLetter():
    
    wiN = GraphWin('text displayer',400,400)
  
    for i in range(10):
   
     texT = input('Enter text here to display:')
     texT2 = texT.split()
  
    for i in texT2: 
  
       click_info = wiN.getMouse()
       intilX = click_info.getX()
       intily = click_info.getY()  
       message = Text(Point(intilX,intily), i)
       message.draw(wiN)
       wiN.getMouse()
 
      #sleep(.2)  
            
      
def singASong():
    
    song_worD = input('Enter songs word:')+' '

    linE = int(input('how many lines you want song to be'))

    timeS = int(input('How many times in single line?'))

    print('below is your song:')

    for i in range(timeS):
    
      s1 = song_worD*linE

      print(s1)
      
def exchangeTable():
        
    for i in range(21):
      
      print('{} exchange rate is :{:0.2f}'.format(i,i*1.17))  
      

def selectFood():
  print("1. Criossant")
  print("2. Pretzel")
  print("3. Taco")
  print("4. Burger")
  print("5. Pizza")
  print("6. Waffles")
  print("7. Ice Cream")
  
  choice = int(input("Please select a food: "))
  
  foods = "🥐🥨🌮🍔🍕🧇🍦"
  
  userFood = foods[choice - 1]
  
  print("You have selected a " + userFood)      

def makeInitialism():
     
 worD = input('\Enter words you wants to instipize :') 
 worD2 = worD.split()
 outpuT = ' '
  
 for i in worD2:
  
  outpuT+= i[0].capitalize()  
 
 print('code is',outpuT)  
   
def nameToNumber():
    
  #for i in range(97,123):
   # print(chr(i), end=" ")    
    
  #for i in range(27):
   # print(i,end=" ")
   
   name = str.lower((input("Enter your name: ")))
   sum = 0
   for char in name:
        sum = sum + ord(char) - 96
   print(sum)
 
                                ##    strings and files   ##
                                
def fileInCaps():
  
  #nameOffile = 'readmefile.txt'
  f = open('readmefile.txt',mode='w',encoding='utf-8')
  #f = f.write().upper()
  #print(f)
  for i in f.read:
    
   y = f.c
   
   #f.readlines()  
   #print(f) 
  
                         
def nameToNumber():
      name = 'sam'
      sum = 0
      
      for i in range(len(name)):
        sum += ord(name[i])-ord('a')+1
     
      print(sum)
      
   
      
nameToNumber()
  
  
  
  
  
  
  
  
   
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          