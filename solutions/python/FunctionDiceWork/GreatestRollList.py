# lists

import random

turnsLeft = 500
val12 = []

def main():
    for i in range(turnsLeft):
        val12.append(greatestRoll())
    print(val12)

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
