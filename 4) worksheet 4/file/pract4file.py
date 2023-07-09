import os

def fileInCaps():
    file_name = input('what name do you want to give?')
    f = open(file_name,"w")
    s=input('write').upper()

    f.write(s)



def read():
    f = open("noyj.txt","r")
    f = f.read()
    print(f)

def  rainfallChart():
    with open('rainfall.txt','r') as file:
        filedata = file.read()
        filedata = filedata.replace('37','**********')
    with open('rainfall.txt','w') as file:
        file.write(filedata)


rainfallChart()




