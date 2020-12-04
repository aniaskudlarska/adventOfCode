#Day 3
#Given a large list representing a map, where . represents empty space and # represents a tree
#each line has a pattern that repeats, and is 31 units long
#Traverse the map by moving RIGHT three spaces DOWN one space
#Map propagates infinitely in the X direction

#Objective 1: Count the number of trees encountered going down
#First, lets load the map into a list of strings
def read_file(filename):
    with open (filename) as inputload:
        return [line.strip() for line in inputload.readlines()]

map = read_file("input3.txt")
print(map)
#Define a function to move the counters one step, and check whether it lands on a tree
#There are two ways to deal with the infinite X axis - propagate the list, or reset it if it overflows
#E.G going 2 above the list of the line places you at the second posistion of the list
#This function only stops when crtY hits len(map)

def getTrees(slope_right, slope_down):
    # Make integers for the X and Y positions on this map, and an int to hold the amount of trees
    ctrX = 0
    ctrY = 0
    trees = 0
    row_length = len(map[0])

    while ctrY < len(map):

        #Check if current item is a tree
        if map[ctrY][ctrX] == '#':
            #print(trees)
            trees += 1
            #print(trees)

        #Increment, and make sure X isnt over using the modulus operator - thanks harrisonmc555!
        ctrX = (ctrX + slope_right) % row_length
        ctrY += slope_down

    return trees

print(getTrees(3,1))

#The second question has different slopes - lets remodel this, and make it variable

#Part 2 - multiply the number of trees encountered on each slope

answer = getTrees(1,1) * getTrees(3,1) * getTrees(5,1) * getTrees(7,1) * getTrees(1,2)
print(answer)

#Solved!