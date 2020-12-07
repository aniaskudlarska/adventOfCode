# Given a list of passwords, return the amount of valid passwords
# Valid passwords have: egl pid eyr hcl byr iyr cid hgt

# Parser will be slightly different - will load the file as one big string, which we then split on newlines
def read_file(filename):
    with open(filename) as inputload:
        return inputload.read().split('\n\n')


# Cleans up the file
def cleanup(cleanlist):
    newList = []
    for item in cleanlist:
        newList.append(item.replace("\n", " "))
    return newList


pass_list = read_file('input4')
uselist = (cleanup(pass_list))


# Dope! Now we make a function to check if a password contains all of the following: 'hcl:' 'iyr:' 'eyr:' 'ecl:'
# 'byr:' 'hgt:' 'pid:'
# Gonna just use a lot of if statements, wont be pretty but hey
# Might be able to make this prettier with regex later

def CheckPass(passtring):
    if 'pid:' in passtring:
        if 'hcl:' in passtring:
            if 'iyr:' in passtring:
                if 'eyr:' in passtring:
                    if 'ecl:' in passtring:
                        if 'byr:' in passtring:
                            if 'hgt:' in passtring:
                                return True
    return False


ctr = 0
for item in uselist:
    if CheckPass(item):
        ctr += 1
# print(ctr)


# Our answer to pt 1 is 228!
# For part 2, we need to add conditionals to each field
# Yeah we're gonna need regex
# Alternatively, for each string, split it into more strings, and if all those strings match, we pass
# TODO: Make this better by making a function of the parsing - I'm too lazy atm, but it could be cleaner
import re


def pid_valid(teststring):
    parsed = re.search('pid:(.*) ', teststring)
    pidtest = (parsed.group(1))
    print(pidtest)
    if len(pidtest) == 9:
        if pidtest.isnumeric():
            return True
    return False


def iyr_valid(teststring):
    parsed = re.search('iyr:(.*) ', teststring)
    iyrtest = parsed.group(1)
    if 2010 <= int(iyrtest) <= 2020:
        return True
    return False


def byr_valid(teststring):
    parsed = re.search('byr:(.*) ', teststring)
    byrtest = parsed.group(1)
    if 1920 <= int(byrtest) <= 2002:
        return True
    return False


def eyr_valid(teststring):
    parsed = re.search('eyr:(.*)', teststring)
    eyrtest = parsed.group(1)
    if 2020 <= int(eyrtest) <= 2030:
        return True
    return False


def ecl_valid(teststring):
    parsed = re.search('ecl:(.*)', teststring)
    ecltest = parsed.group(1)
    valid_eyr = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    for n in valid_eyr:
        if ecltest == n:
            return True
    return False

def hgt_valid(teststring):
    parsed = re.search('hgt:(.*) ', teststring)
    hgttest = parsed.group(1)
    numbers = re.findall(r'\d+', hgttest)
    if hgttest[-3:] == 'in ': #Replace this line with regex
        print("hit")
        if 59 <= int(numbers[0]) <= 76:
            return True
    return False

print(hgt_valid('hgt:60in hgthg;ldfbk'))

#TODO: Finish valid checkers and function

def hcl_valid(teststring):
    parsed = re.search('hcl:(.*) ', teststring)
    hcltest = parsed.group(1)
    numbers = re.findall(r'\d+', hcltest)
    if hcltest[0] == '#':
        if len(numbers[0]) == 6:
            if numbers[0].isnumeric:
                return True

    return False

print(hcl_valid("hcl:#111111 "))



