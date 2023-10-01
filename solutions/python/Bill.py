# if, elif, else, user input terminal

season = input(
    """
    For what season are you estimating the bill?
    Enter
        A for Summer
        B for Fall
        C for Winter
        D for Spring
    """)

print("You entered", season)

house = int(input(
    """
    What type of house do you have?
    Enter
        1 for Single
        2 for Duplex
        3 for Row
    """))

print("You entered", house)

if season == "A":
    centralAir = input("Do you want central air? Y/N")
    if house == 1:
        if centralAir == "Y":
            print("$200.00")
        else:
            print("$50.00")
    elif house == 2:
        if centralAir == "Y":
            print("$150.00")
        else:
            print("$40.00")
    else:
        if centralAir == "Y":
            print("$125.00")
        else:
            print("35.00")
elif season == "B" or season == "D":
    if house == 1: 
        print("$50.00")
    elif house == 2:
        print("$40.00")
    else: 
        print("$35.00")
else:
    if house == 1:
        print("$250.00")
    elif house == 2:
        print("$200.00")
    else:
        print("$175.00")
        
