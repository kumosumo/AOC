from pyreadline3 import Readline
readline = Readline()

file = open('input.txt', 'r')
lines = file.readlines()

m = 0 
total = 0
cals = []
for line in lines:
    if line == '\n':
        if total > m:    
            m = total
        print(total)
        cals.append(total)
        total = 0
    else:
        total +=int(line)
print("Solution: " + str(m))
cals = sorted(cals, key= int, reverse=True)
print("Sum of biggest 3" + str(sum(cals[0:3])))
print(sum(cals[0:3]))
print((cals[0:3]))