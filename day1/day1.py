#Given a list of strings, find the two entries that sum to 2020, and then return their product

listInput = [] #


#Load all numbers from input.txt into a list
with open ('input.txt', 'r') as inputF:
    for f in inputF:
        listInput.append(f)

#Going to try doing this in 3 steps (is this the fastest time? prolly not, big O was never my thing lol)
#1) Select the first item in the list, listInput[0]
#2) Check it against every other entry in the list, listInput[1....-1]
#3) If they sum to 2020, return their product
#4) If none do, start again from listInput[n+1]

#The code below doesnt work, and i'm not sure how to fix it - leaving it here for posterity

def recursiveSolve(testNumber):
    while testNumber < len(listInput): #First loop, till testNumber hits the end of list
        testNumber = 0  # initial number

        #def innerLoop(): #Second loop, till ctr hits end of list. When it does, increment testNumber and start again
        ctr = testNumber + 1  # Number to multiply by
        while ctr < len(listInput):
                if listInput[testNumber] + listInput[ctr] == 2020:
                    print("Condition filled")
                    print(listInput[testNumber] * listInput[ctr])
                    return listInput[testNumber] * listInput[ctr]
                else:
                    #print("Hit this")
                    ctr +=1

        print(testNumber)
        testNumber += 1

    return("Failed to print")
#print(recursiveSolve())

#Ultimately, I just solved it with nested for loops!

def secondSolve():
    for item in listInput:
        for item2 in listInput:
            if int(item) + int(item2) == 2020:
                return int(item) * int(item2)

print(secondSolve())
