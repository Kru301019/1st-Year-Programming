from random import randint


def tenCoinFlips():
    
   ran =  randint(1 ,2)
   print(ran)
   for i in range(10):
       if ran == 1:
           print('Heads')
       else:
           print('Tails')


tenCoinFlips()
