import re 
import os
import csv

os.chdir(os.path.dirname(os.path.realpath(__file__)))

from Sixers import Sixer

Sixers = []

with open("Sixers.csv") as csvFile:
    reader = csv.reader(csvFile)
    line_count = 0
    for x in reader:
        if line_count != 0:
            id = re.sub(r"[^0-9]", "", x[0])
            #names = re.sub(r"\d", "", x[1])
            nameparts = re.split(r"\s+", x[1], 1)
            Sixers.append(Sixer(id=id, firstName = nameparts[0], lastName = re.sub(r"\d", "", nameparts[1]), number = re.sub(r"[A-Za-z]", "", nameparts[1]),
                          position = x[2], age = x[3], height = Sixer.heightToMeters(x[4]),
                          weight = Sixer.lbstoKilograms(x[5]), college = x[6], salary = x[7] ))
        line_count += 1

for player in Sixers:
   print("Last Name: {} \n Age: {} \n Salary: {} \n Number: {}".format(player.lastName, player.age, player.salary, player.number))

user = input("Enter a player number (e.g. 32): ")
try:
   chosen = next(player for player in Sixers if player.number == user)
   import webbrowser
   webbrowser.open(chosen.genURL(), new=2)
except:
   print("\nThat might not be a player number. ")
