# This is a sample Python script.
from PIL import Image
import os

from os import listdir
from os.path import isfile, join

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def openimage():
    filepath = os.getcwd()
    print(filepath)
    filepath+= "\\truth.PNG"

    img = Image.open(r"C:\Users\padop\PycharmProjects\ImageSorter\pizza.jpg")

    img.show()

def getdir():
    print("Would you like to use the current directory or a custom one? (CURR/CUST)")
    inputval = input()
    if ((inputval == 'CURR') | (inputval =='current') | (inputval =='CURRENT') | (inputval =='Current') | (inputval =='curr')):
        print("Using current directory...")
        inputval = os.getcwd()
    else:
        inputval = input("Custom directory:")
        #check if they inputted a \ at the end
        if (inputval[len(inputval)-1] != '\\'):
            inputval+=('\\')
        print("Using custom directory:",inputval)

    return inputval

def getimages(filelist):

if __name__ == '__main__':

    dir = getdir()

    onlyfiles = [f for f in listdir(dir) if isfile(join(dir, f))]

    print(onlyfiles)
    inputval = ""
    while (inputval != 'exit'):
        inputval = input("New filename:")
    print("done")
