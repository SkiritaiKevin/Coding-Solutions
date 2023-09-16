# Description of problem can be found in docx file
# N/A

scores = [78, 98, 86, 57, 92, 88]

def small(k, *args):
    myList = list(args)
    myList.sort()
    minVal = myList[k-1]
    return minVal

print(small(1,*scores))
print(small(2,*scores))
print(small(3,*scores))
