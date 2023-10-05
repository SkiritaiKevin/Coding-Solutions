# Kevin Beideman

# Have user input a GPA (which is an float)

'''
 determine between 
    Summa cum laude >= 3.8
    Magna cum laude >= 3.6
    Cum laude >= 3.4
    Graduating >= 2.0
    Not graduating
'''

userGPA = float(input("Input your GPA"))

if userGPA > 4.0 or userGPA < 0:
    print("out of range")
elif userGPA >= 3.8:
    print("summa cum laude")
elif userGPA >= 3.6: 
    print("magna cum laude")
elif userGPA >= 3.4:
    print("cum laude")
elif userGPA >= 2.0:
    print("graduating")
else:
    print("not graduating")