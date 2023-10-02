#list parameters

goals = [20, 37, 8, 17, 55, 82]
print(goals)
print(type(goals))
print(*goals)

def avgGoals(values):
    sum = 0
    for i in values:
        sum+=i 
    return sum/len(values)

print(goals)
print(avgGoals(goals))

def avgGoals2(*values):
    sum = 0
    for i in values:
        sum+=i
    return sum/len(values)

print(avgGoals2(1,2,3,4))
print(avgGoals2(*goals))