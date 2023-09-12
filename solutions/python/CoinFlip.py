# Assignment for CSC 341 (Open Software Application Development)
# N/A

import random
import statistics 

def coinFlip(): # heads will act as 0 and tails will act as 1 
    flips = 0 
    coin1 = random.randint(0,1); 
    coin2 = random.randint(0,1); 
    coin3 = random.randint(0,1); 
    coin4 = random.randint(0,1);
    coin5 = random.randint(0,1);

    while not(coin1 == coin2 == coin3 == coin4 == coin5):
        coin1 = random.randint(0,1)
        coin2 = random.randint(0,1)
        coin3 = random.randint(0,1) 
        coin4 = random.randint(0,1)
        coin5 = random.randint(0,1)
        flips += 1

    return flips

def dictGen(*args):
    #easier way to find data https://docs.python.org/3/library/statistics.html
    flipStats = {}

    average = statistics.mean(results)
    flipStats["average"] = average

    standardDev = statistics.stdev(results)
    flipStats["standard deviation"] = standardDev

    minimum = min(results) # note that the min can be 0 if they all are the same face first try, since I roll them before the while loop clause
    flipStats["minimum"] = minimum

    maximum = max(results)
    flipStats["maximum"] = maximum

    median = statistics.median(results)
    flipStats["median"] = median

    return flipStats
    

sampleSize = int(input("How many times do you want to call the Coin Flip function?"))
results = []
for _ in range(sampleSize):
    flipCount = coinFlip()
    results.append(flipCount)

statList = dictGen(*results)
print(statList)






