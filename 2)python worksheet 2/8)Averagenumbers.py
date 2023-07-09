from ast import Num
from itertools import count
import math
sum=0
inp=int(input('how many numbers'))
for i in range(inp):
 count=int(input('Enter number'))
 sum=sum+count
 average=sum/inp
print('sum is',average)
