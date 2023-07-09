import math
#x1,y1,x2,y2=input('Enter four values').split()
x1=int(input('Enter values of x1:'))
y1=int(input('Enter values of y1:'))
x2=int(input('Enter values of x2:'))
y2=int(input('Enter values of y2:'))
print('values of x1:',x1)
print('values of y1:',y1)
print('values of x2:',x2)
print('values of y2:',y2)
slope1=y2-y1
slope2=x2-x1
slope=slope1/slope2
#slope=y2-y1/x2-x1
print('Slope of line is-}',slope)