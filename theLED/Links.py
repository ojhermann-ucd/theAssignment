import urllib.request
from urllib.error import URLError, HTTPError
from venv import create
import theLED.Grid as Grid

#validLink
def validLink(theLink):
    try:
        theSource = urllib.request.urlopen(theLink)
        return True
    except ValueError:
        return False
    except HTTPError:
        return False
    except URLError:
        return False
    else:
        return False

def createLinkList(linkSource): #input string reference to document
    linkList = []
    with open(linkSource) as theSource:
        for line in theSource:
            cleanLine = line.rstrip('\n')
            if validLink(cleanLine):
                linkList.append(cleanLine)
    return linkList #list