from theLED.Grid import *
from theLED.Instructions import *

def modificationEntry(theI, theBool): #Instruction and boolean inputs
    if theI.command == "on":
        return True
    if theI.command == "off":
        return False
    if theI.command == "switch":
        return not theBool

def modificationGrid(theI, theG): #instructions and grid
    for x in range(theI.x1, theI.x2 + 1, 1):
        for y in range(theI.y1, theI.y2 + 1, 1):
            xyTuple = (x, y)
            xyBool = theG.get(xyTuple,)
            theG[xyTuple] = modificationEntry(theI, xyBool)
    return theG