import math

def getFuel(mass):
    return math.floor(int(mass)/3)-2

sum = 0

with open("day_1_input.txt", "r") as r:
    for line in r.readlines():
        moduleFuel = getFuel(line)
        sum += moduleFuel
        newFuel = moduleFuel 
        while 1:
            temp = newFuel
            newFuel = getFuel(temp)
            if(newFuel <= 0):
                break
            sum += newFuel

print(sum)