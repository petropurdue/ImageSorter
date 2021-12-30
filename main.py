# This is a sample Python script.
from PIL import Image
import os

from os import listdir
from os.path import isfile, join


def openimage(dir,suffix):
    path = dir + suffix

    img = Image.open(path)
    img.show()
    print("New filename for:",suffix)
    inputval = input()

    img.close()
    return inputval

def getdir():
    print("Would you like to use the current directory or a custom one? (CURR/CUST)")
    inputval = input()
    inputval = inputval.lower()
    if ((inputval == 'curr') | (inputval =='current')):
        print("Using current directory...")
        inputval = os.getcwd()
        inputval += ('\\')
    else:
        inputval = input("Custom directory:")
        #check if they inputted a \ at the end
        if (inputval[len(inputval)-1] != '\\'):
            inputval+=('\\')
        #print("Using custom directory:",inputval)

    inputval = inputval.replace('\\','/')
    print("Using directory:", inputval)
    return inputval

def getimages(filelist):
    finlist = []
    for i in filelist:
        lngth = len(i)
        extension = (i[(lngth-4):(lngth)])
        extension = extension.lower()
        if ((extension == '.png') | (extension == '.jpg')): #| if I add support for jpeg, I will need to change the renaming part of main (extension == 'jpeg')
            finlist.append(i)
    return finlist

if __name__ == '__main__':
    #initializations
    inputval = ""

    #RENAME MODE
    dir = getdir()

    onlyfiles = [f for f in listdir(dir) if isfile(join(dir, f))] #thanks to pycruft from https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory

    imgs = getimages(onlyfiles)

    print("To keep the filename, simply press space")
    print("To stop filenaming, enter 'exit'")

    for suffix in imgs:
        response = openimage(dir,suffix)

        #check if it exit
        if response == 'exit':
            break
        #check rename
        if response != ' ': #sets it up so that if it is not the space needed to reset, rename the file. OW, proceed to next file
            path = dir + suffix
            extension = (suffix[(len(suffix) - 4):(len(suffix))])

            os.rename(path,dir+response+extension)
            #print(dir+response+extension)



    print("done")
