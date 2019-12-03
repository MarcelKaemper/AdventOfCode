import math

def getFuel(mass):
    return math.floor(int(mass)/3)-2

sum = 0

with open("day_1_input.txt", "r") as r:
    for line in r.readlines():
        sum += getFuel(line)

print(sum)