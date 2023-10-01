# def main(), if __name__ == '__main__'

import random

turnsLeft = 500

def main():
    sum = 0
    for i in range(turnsLeft):
        maxVal = greatestRoll()
        print("Two sixes after {} rolls".format(maxVal))
        sum += maxVal
    print("Average amount of rolls to get the greatest value was {}".format(sum/turnsLeft))  

def greatestRoll():
    rolls = 0
    die1 = 0
    die2 = 0
    while die1 + die2 != 12:
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        rolls+=1
    return rolls

if __name__ == '__main__':
    main()

