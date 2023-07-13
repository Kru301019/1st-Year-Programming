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


def drawHexagon():
    win = 
