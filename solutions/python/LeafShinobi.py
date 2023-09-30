# scenario: check if user entry is a leaf shinobi
# lists, user terminal input, for loops, .index(), enumerate()

lsFirst = ["Naruto", "Sasuke", "Kakashi", "Minato"]
lsLast = ["Uzumaki", "Uchiha", "Hatake", "Namikaze"]

print("HALT. This is the border of the Village Hidden in the Leaves. \n What is your name?")
fnAttempt = input("First Name: ")
lnAttempt = input("Last Name: ")

found = False
for i, shinobi in enumerate(lsFirst):
    if fnAttempt == shinobi and lnAttempt == lsLast[i]:
        print("Good Credentials. You may enter.")
        found = True
        break
if not found:
    print("You're an outsider. You may not enter.")

print("")

fnAttempt2 = input("2. First Name: ")
lnAttempt2 = input("2. Last Name: ")

if fnAttempt2 in lsFirst:
    fnIndex = lsFirst.index(fnAttempt2)
    if lnAttempt2 == lsLast[fnIndex]:
        print("Good Credentials. You may enter.")
    else:
        print("You're an outsider. You may not enter.")
else:
    print("You're an outsider. You may not enter.")
