import urllib.request
from urllib.error import URLError, HTTPError

#turns input into a list after removing leading whitespace
def gridInputRemoveLeftWhiteSpace(str): #string input
    str = str.lstrip()
    str = str.lstrip('b')
    str = str.split() 
    return str #returns a list

#checks if length is one i.e. only one number was given
def gridCheckLength(theList): #list input
    return (len(theList) == 1) #boolean output

#checks if the entry is a number
def gridCheckInt(theList): #list input
    try:
        theInt = int(theList[0])
        return isinstance(theInt, int) #boolean output
    except ValueError:
        return False

#generates the integer
def gridMakeInt(theList): #list input
    return int(theList[0]) #int output

#makes sure theInt is positive
def gridCheckIntSign(theInt): #int input
    return (theInt > -1) #boolean output

def gridCheckIntSize(theInt):
    return (theInt < 10**9)

def gridCreateSizeList(sourceList): #input list
    gridSizeList = []
    for source in sourceList:
        theSource = urllib.request.urlopen(source)
        with theSource as theSrc:
            theSrc = theSrc.readline().decode('utf-8')
            theSrc = gridInputRemoveLeftWhiteSpace(theSrc)
            #tests
            if not (gridCheckLength(theSrc) and gridCheckInt(theSrc) and gridCheckIntSign(gridMakeInt(theSrc)) and gridCheckIntSize(gridMakeInt(theSrc))):
                gridSizeList.append("n/a")
            else:
                gridSizeList.append(theSrc[0])
    return gridSizeList

class Grid: #creates the grid with initial values of False

    def __init__(self, num):
        self.rows = int(num)
        self.columns = int(num)
        self.grid = self.generateGrid()
        self.size = (int(num) + 1) ** 2

    def generateGrid(self):
        theGrid = {}
        row = 0
        column = 0
        while row <= self.rows:
            while column <= self.columns:
                theGrid[(row, column)] = False
                column += 1
            column = 0
            row += 1

        return theGrid