
s='Hello '
s2='world at war' 
##join strings
print(s+s2)

##count lenth of characters

print(len(s+s2))

## print the whole world


print(s2[0])  #0,1,2,3,4,,5


##print certain words one by one

for index in range(12):
   print(s2[index])
s='helloworld'                                #h e l l o w o r l d
                                              #0 1 2 3 4 5 6 7 8 9
                                          #   -10-9-7-6-5-4-3-2-1 
print(s[1:6])

##count from backwards 

print(s[1:-6])

for ch in 'sam':
    print(ch)

from re import S

n=[1,3,5,7,8,9]
s='hello world'
for ch in s:
    print(ch)
for numb in n:
    print(numb)
    print(n)    
 
##capatilize word

s='hello world'

s2=s.upper()
print(s2)

##replae words

s='hello world'
s2=s.replace('hello','bye')
print(s2)

s='hello world'
s2=s.split()
print(s2)
for i in s2:
    print(s2)


s='hello'

print('count is:',s.count('e'))

s='hello world'

##split it 

s2=s.split()

for i in s2:
    print(i)
    
    
##formatting 

x = 10.123456789
y = 20
print("The values are {0:0.4f} and {1:8}.".format(x, y))    
    
    
    
    
    