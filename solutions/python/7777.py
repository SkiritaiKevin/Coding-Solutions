# for loops, random class

import random

text = "7 + 7 + 7 + 7 + 7 + 7 + 7? "

# what is range?

exampleRange = range(5) # 0, 1, 2, 3, 4            i < numbers.length; 
for i in exampleRange:
    print(i)

paragraphs = random.randint(6, 8)
for pargraph in range(paragraphs):
    sentences = random.randint(10, 15)
    for sentence in range(sentences):
        print(text, end="")
    print("\n")
print("Haha......HAHAHAHAHAHAHA!!!!!!!!!!")