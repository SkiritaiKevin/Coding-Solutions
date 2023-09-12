# Assignment for CSC 341 (Open Software Application Development)
# N/A

import os 

os.chdir(os.path.dirname(os.path.realpath(__file__)))

# parallel lists for later 
employees = []
ques1 = []
ques2 = []
ques3 = []
ques4 = []
ques5 = []
ques6 = []


with open("COVID_survey.csv", "r") as file1: 
    for line in file1:
        if line.strip():
            removeComma = line.rstrip().split(",")
            employees.append(removeComma[0])
            ques1.append(int(removeComma[1]))
            ques2.append(int(removeComma[2]))
            ques3.append(int(removeComma[3]))
            ques4.append(int(removeComma[4]))
            ques5.append(int(removeComma[5]))
            ques6.append(int(removeComma[6]))

employeesIn = []

for i in range(len(employees)):
    # ques 1 must always be 1, but just one from 2-6 need to be 1
    if ques1[i] == 1 and (ques2[i] == 1 or ques3[i] == 1 or ques4[i] == 1 or ques5[i] == 1 or ques6[i] == 1):
        employeesIn.append(employees[i])

print("Employees who have decided to come in and have answered at least yes to one of the question in range (2-6) are as follows:")
for i in employeesIn: #loop through list and print names
    print(i)
