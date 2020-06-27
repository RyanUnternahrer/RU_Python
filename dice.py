import random as rnd

i = 0

numTimes = input("How many times would you like to roll the die? ")
numTimes = int(numTimes)
while numTimes > i:
     num = rnd.randrange(6)
     num = num + 1
     print("Roll:", num)
     i = i + 1
