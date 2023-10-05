# Kevin Beideman

import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Write a PACity class with properties city, county, population,
# medianHouseHoldIncome, perCapitaIncome
'''
   Add a method that uses code like 
   that multiplies population and perCapita income to get totalIncome
'''


class PACity:
   def __init__(self, city, county, population, medianHouseIncome, perCapitaIncome):
      self.city = city
      self.county = county
      self.population = population
      self.medianHouseIncome = medianHouseIncome
      self.perCapitaIncome = perCapitaIncome
   
   def totalIncome(pop, pci):
      product = pop * pci
      return product



# Read the file PA_City.csv
# Create a list of City objects
Cities = []

import csv
with open("PA_City.csv") as csvFile:
   #print("here")
   reader = csv.reader(csvFile)
   #print("2nd")
   line_count = 0
   for x in reader:
      #print("hello")
      if line_count != 0:
         #print("yo")
         Cities.append(PACity(city=x[0], county=x[1], population=int(x[2]), medianHouseIncome=int(x[3]), perCapitaIncome=int(x[4])))
      line_count+=1

# Loop through the list of cities,
# display city, county, population and total income (using method)

for city in Cities:
   #print("{}".format(PACity.totalIncome(city.population, city.perCapitaIncome)))
   print("City: {} \n County: {} \n Population: {} \n Total Income {}".format(city.city, city.county, city.population, PACity.totalIncome(city.population, city.perCapitaIncome)))