#imports
import sys
import theLED.Grid as Grid
import theLED.Instructions as Instructions
import theLED.Modification as Modification
import theLED.Links as Links
import urllib.request
from urllib.error import URLError, HTTPError
from itertools import islice
import io
import time
import argparse
from builtins import str

#argparse stuff
parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()

group.add_argument("-u", "--url", action="store_true")
group.add_argument("-f", "--file", action="store_true")

parser.add_argument("source", help="url or file")
args = parser.parse_args()

#create sourceList
if args.url:
    sourceList = []
    sourceList.append(args.source)
else:
    sourceList = Links.createLinkList(str(args.source))

#sourceList = Links.createLinkList("LinksSource.txt")

#create gridSizeList
gridSizeList = Grid.gridCreateSizeList(sourceList)

#function for summing the values of the grid
def sumLED(gridSize, theSource): #int, str
    theGrid = Grid.Grid(gridSize).grid
    theSource = urllib.request.urlopen(theSource)
    for line in theSource:
        theLine = str(line, 'utf-8')
        #formatting
        theLine = Instructions.instructionFormat(theLine)
        #test
        if not Instructions.instructionValidTypes(theLine):
            pass
        else:
            theLine = Instructions.instructionValidRange(theLine, gridSize)
            if not Instructions.instructionValidOrder(theLine):
                pass
            else:
                theLine = Instructions.Instruction(theLine)
                theGrid = Modification.modificationGrid(theLine, theGrid)
    gridSum = sum(theGrid.values())
    return gridSum

#do it
count = 0
for g in gridSizeList:
    #startTime = time.time()
    if g == "n/a":
        print(sourceList[count], g)
    else:
        print(sourceList[count], sumLED(int(g), sourceList[count]))
        #print(time.time() - startTime)
    count += 1