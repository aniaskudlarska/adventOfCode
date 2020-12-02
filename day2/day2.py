#Day 2
#Parse a string formatted like INT-INT char: string
#e.g 1-3 a: abcde
#extract 3 variables: minVal, maxVal, char
#Return TRUE iff char appears > minVal and < maxVal

#TODO: Solve this again with regex

import re

def isValid(passwordInput):
    #Ok, new strategy - use split to split into inputLine and parseLine
    lineSplit = passwordInput.split(": ")
    inputLine = lineSplit[0]
    parseLine = lineSplit[1]

    #inputLine is the password rule, formatted ex. "1-3 a"
    #parseline is the line to be parsed ex "abcde"

    #now we extract char - it's always the last index in inputLine
    char = inputLine[-1]

    #Now we extract positive integers from inputLine
    values = [int(s) for s in re.findall(r'\d+', inputLine)]

    #Min is the first number, max is the second]
    minVal = values[0]
    maxVal = values[1]

    #now we parse parseLine, using count()
    ctr = parseLine.count(char)
    if ctr >= minVal and ctr <= maxVal:
        return True

#Now we use this function on each string in a list, reading an input.txt file
#Returns the amount of valid passwords in a list
def readInput():
    ctr = 0
    with open("input.txt", 'r') as inputFile:
        inputLines = inputFile.readlines()
    for n in inputLines:
        if isValid(n):
            ctr+=1
    return ctr

print(readInput())

#That solves Part One!

#Part 2: different formatting - indexes instead of occurences
#e.g 1-3 a: valid if ONE of posistion 1 or 3 contains char

#Copypasting above code, with minor edits
def isValid2(passwordInput):
    lineSplit = passwordInput.split(": ")
    inputLine = lineSplit[0]
    parseLine = lineSplit[1]

    char = inputLine[-1]

    values = [int(s) for s in re.findall(r'\d+', inputLine)]

    pos1 = values[0]
    pos2 = values[1]
    #Also, in this arbitrary puzzle we shift indexes over by -1

    #there's probably a more pythonic way to write this
    if parseLine[pos1-1] == char and parseLine[pos2-1] != char:
        return True

    if parseLine[pos1-1] != char and parseLine[pos2-1] == char:
        return True

#Now to run this over the list

def readInput2():
    ctr = 0
    with open("input.txt", 'r') as inputFile:
        inputLines = inputFile.readlines()
    for n in inputLines:
        if isValid2(n):
            ctr+=1
    return ctr

print(readInput2())

#Parts 1 and 2 solved! [524,485]