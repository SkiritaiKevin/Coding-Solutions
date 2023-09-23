# video displaying ifs, else if, else, nested ifs, boolean AND, some terminal work

firstName = "Light"
lastName = "Yagami"


firstNameAttempt = input("What is Kira's first name?")
lastNameAttempt = input("What is Kira's last name?")

if firstNameAttempt == firstName:
    if lastNameAttempt == lastName:
        print("You guessed right.")
    else:
        print("Wrong.")
else:
    print("Wrong.")


firstNameAttempt = input("What is Kira's first name?")
lastNameAttempt = input("What is Kira's last name?")

if firstNameAttempt == firstName and lastNameAttempt == lastName:
    print("You guessed right.")
else:
    print("Wrong.")
