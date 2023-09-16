# Description in docx file
# N/A

import os

os.chdir(os.path.dirname(os.path.realpath(__file__)))

planets = []
periods = []
distanceToSun = []

with open("Kepler.csv", "r") as file1: 
    for line in file1:
        if line.strip():
            removeComma = line.rstrip().split(",")
            planets.append(removeComma[0])
            periods.append(float(removeComma[1]))
            distanceToSun.append(float(removeComma[2]))

for i in range(len(periods)):
    result = (periods[i] * periods[i]) / (distanceToSun[i] * distanceToSun[i] * distanceToSun[i])
    print("{} {} {} T^2/a^3={}".format(planets[i], periods[i], distanceToSun[i], result))
