# Day 4 part one

sum = 0

for num in range(240298,784956):
    num = list(str(num))
    adj = False
    sm = False
    if(len(num) == 6):
        for i in range(len(num)-1):
            x = int(num[i])
            if(int(num[i+1])<x):
                sm = True
                break
            if(int(num[i+1])==x):
                adj = True
            prev = int(x)
    if adj and not sm:
        sum += 1

print(sum)