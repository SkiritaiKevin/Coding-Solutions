# keep rolling until both dies = to 6 and get some info from that
# for loop, while loop

import random

turnsLeft = 500
sum = 0

for i in range(turnsLeft):
    rolls = 0
    die1 = 0
    die2 = 0
    while die1 + die2 != 12:
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        rolls+=1
    print("Snake eyes after {} rolls".format(rolls))
    sum += rolls
print("Average amount of rolls to get the greatest value was {}".format(sum/turnsLeft))
