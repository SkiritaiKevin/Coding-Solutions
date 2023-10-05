# Kevin Beideman

scores = [87, 97, 86, 58, 92, 79]
scores2 = [1, 2, 3]

# replace word pass below with your code 
# that returns the sum of the scores raised to the kth power 
def moment(k, *args):
    sum = 0
    lis = list(args)
    for number in lis:
        sum += number**k
    return sum
    

print(moment(1, *scores))  
print(moment(2, *scores))

print(moment(1, *scores2))  
print(moment(2, *scores2))  
print(moment(3, *scores2))  