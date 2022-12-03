from pyreadline3 import Readline
readline = Readline()

file = open('input.txt', 'r')
lines = file.readlines()

outcomes = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1, 
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6,
}
outcomes2 = {
    "B X": 1,
    "A X": 3,
    "C X": 2,
    "A Y": 4,
    "B Y": 5,
    "C Y": 6,
    "A Z": 8,
    "B Z": 9,
    "C Z": 7,
}
sum = 0 
for line in lines:
    sum += outcomes.get(line.strip())
print(sum)
sum = 0 
for line in lines:
    sum += outcomes2.get(line.strip())
print(sum)