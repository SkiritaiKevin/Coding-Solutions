# my video on if, else if, else

# A ghoul: 5 human kills
# S ghoul: 20 human kills
# SS ghoul: 100 human kills
# SSS ghoul: 10000 human kills

numKills = int(input("How many humans have you killed?"))

if numKills >= 5 and numKills < 20:
    print("A tier ghoul.")
elif numKills >= 20 and numKills < 100:
    print("S tier ghoul.")
elif numKills >= 100 and numKills < 10000:
    print("SS tier ghoul.")
elif numKills >= 10000: 
    print("THREAT: SSS tier ghoul.")
else:
    print("Low tier ghoul. Easy eradication.")
