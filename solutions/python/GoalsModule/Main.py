import Goals as goalMod

goals = [20, 37, 8, 17, 55, 82]

result = goalMod.goalStats(*goals)
print(result)
print("The average is {:.3f}".format(result["mean"]))