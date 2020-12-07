# TODO

# Given a 10 character string with F, B, L, R, use binary space partitioning
# to find which of the rows from 1 to 128 on a plane a code corresponds to
# e.g FBFBBFFRLR:
# 0) Start with the whole range, 0 to 127
# 1) F means lower half, 0 thru 63
# 2) B means upper half, 32 thru 63
# 3) F means lower half, meaning 32 thru 47
# 4) B means upper half, meaning 40 thru 47
# 5) B Keeps 44 thru 47
# 6) F keeps 44 thru 45
# 7) final F keeps 44

# Last 3 characters specify list from 0 to 7
# R keeps upper half, 4 thru 7
# L keeps lower half, 4 thru 5
# R keeps 5

# This would return 44, 5
# Also return seat ID which is row * 8 + column


# My code was messy, and tried to use lists - I cleaned it up by borrowing from
# https://dev.to/qviper/advent-of-code-2020-python-solution-day-5-117d
# Thanks Viper!

# First, let's parse inputs into a list of strings

inputfile = open('input5', 'r')
data = [x.strip() for x in inputfile.readlines()]


# Helper functions to split a list in half and return first or second half
# Deprecated, used a different solution
def getFirstHalf(inlist):
    length = len(inlist)
    midpoint = (length // 2)
    return inlist[:midpoint]


def getSecondHalf(inlist):
    length = len(inlist)
    midpoint = (length // 2)
    return inlist[midpoint:]


def getBoardingPass(inputstring):
    # This might be a messy way of doing it, but let's make a list of all numbers btw seatmin and seatmax
    # and keep splitting that list
    row,col = 0,0

    parseline = inputstring[:7]
    start = 0
    end = 127
    for n in parseline:
            if n == "F":
                end = int((start+end+1)/2)-1
                #print(end)
            elif n == "B":
                start = int((start+end+1)/2)

    row = start

    parseline = inputstring[7:]
    start = 0
    end = 7
    for n in parseline:
            if n == "L":
                end = int((start+end+1)/2) -1
            elif n == "R":
                start = int((start+end+1)/2)
    col = start
    # print(rowList)
    sid = row*8 + col

    # ID = (valList[0] * 8 + int(rowList[0]))
    # boardingPass.append(ID)
    return row,col,sid


def getBoardingPassList(datalist):
    bpList = []
    for n in datalist:
        bpList.append(getBoardingPass(n))

    return bpList


BPList = getBoardingPassList(data)
#BFFFBFFLRL
# 0 127
# 63 127 B
# 63 95 F
# 63 79 F
# 63 71 F
# 67 71 B
# 67 69 F
# 68 69 F
# 68
#for n in BPList:
 #   (print(n))
BPList.sort()
#print(len(BPList))

#First solution: 935
#second solution: 743

#Second problem: Find your seat
#Find the missing boarding pass - seats at front and back dont exist
#I.E seats where the first value is 0 or 127

seat_ids = []
for n in BPList:
    seat_ids.append(n[2])

solution = [seat for seat in range(min(seat_ids),max(seat_ids)) if seat not in seat_ids][0]
print(solution)
