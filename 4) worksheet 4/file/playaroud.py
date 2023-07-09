import os

'''
msg = "abc"
for char in msg:
  print("character is {} and its numerical equivalent is {}".format(char,ord(char)))
'''

def fileInCaps():
    os.getcwd()   #import os find out full path
    os.listdir()  #To obtain a list of the names of the files and subfolders within this folder, do:
    os.chdir("")

def readingfiles():

def read():
    f = open("nothin.txt","r")
    f = f.read()
    print(f)

    #read the entire contents
    content = infile.read()
    print(content)

    #Close the file with:
    close = inFile.close()
    print(close)


def readline():
    infile = open("quotation.txt", "r")
    line = infile.readline() #readlines will read all lines in as separe string
    print(line)

def readfilewithloop():
        inFile = open("quotation.txt", "r")
        for line in inFile:
           print(line)
        inFile.close()

def write_file():#createempteyfile
    outFile = open("myfile.txt", "w")

def write_inside_file():

    f = open("efqew.txt", "a")
    s ="what do you need is it not enough?\n"
    f.write(s) #writelines
    f.close()

write_inside_file()





