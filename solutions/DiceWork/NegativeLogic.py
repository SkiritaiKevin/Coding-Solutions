# end when sum = 2 or 12
# de morgans theorem

import random

die1=0
die2=0

count=0
while die1+die2 != 2 and die1+die2 != 12:
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    count+=1
print(count)


count=0
while True:
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    count+=1
    if die1+die2 == 2 or die1+die2 == 12:
        break
print(count)

