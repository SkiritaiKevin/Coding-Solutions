# video on if, elif, else + dictionary 

# i want to suggest a random anime

import random

#first approach 

draw = random.randint(1, 12)
print("Draw: {}".format(draw))

if draw == 1: 
    print("Naruto")
elif draw == 2:
    print("Attack on Titan")
elif draw == 3: 
    print("Sword Art Online")
elif draw == 4:
    print("Hunter X Hunter")
elif draw == 5:
    print("One Punch Man")
elif draw == 6:
    print("Demon Slayer")
elif draw == 7:
    print("Death Note")
elif draw == 8:
    print("Tokyo Ghoul")
elif draw == 9: 
    print("One Piece")
elif draw == 10:
    print("Blue Lock")
elif draw == 11: 
    print("My Happy Marriage")
else:
    print("Food Wars")


# second approach

animes = {
    1:"Naruto",
    2:"Attack on Titan", 
    3:"Sword Art Online", 
    4:"Hunter X Hunter", 
    5:"One Punch Man", 
    6:"Demon Slayer",
    7:"Death Note", 
    8:"Tokyo Ghoul",
    9:"One Piece", 
    10:"Blue Lock", 
    11:"My Happy Marriage",
    12:"Food Wars"

}

pick = random.randint(1,12)
print("Pick: {}".format(pick))
print(animes.get(pick))
