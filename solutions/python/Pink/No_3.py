# Kevin Beideman

import os

os.chdir(os.path.dirname(os.path.realpath(__file__)))
# to be the directory of this program's file

# declare lists for country names, birth rates and death rates 

countries = []
birthRates = []
deathRates = []
# Read and parse file Country.csv 
# use data to set list values

with open("Country.csv", "r") as csvFile:
    for line in csvFile:
        if line.strip():
            x = line.rstrip().split(",")
            countries.append(x[0])
            birthRates.append(float(x[1]))
            deathRates.append(float(x[2]))

for i in range(len(countries)):
    difference = birthRates[i] - deathRates[i]
    status = ""
    if difference >= 10:
        status = "Growing rapidly"
    elif 0 <= difference < 10:
        status = "Growing"
    else:
        status = "Shrinking"
    print("Country: {} Birth Rate: {} Death Rate: {} Difference: {} Cat: {}".format(countries[i], birthRates[i], deathRates[i], difference, status))

# Print out info include a "difference" birth_rate - death_rate as well as a category
'''
Growing rapidly 	if diff >= 10
Growing rapidly	if 0 <= diff <10
Shrinking		   if diff <0
''' 

