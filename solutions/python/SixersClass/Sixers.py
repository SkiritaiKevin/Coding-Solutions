import re 

class Sixer:
    def __init__(self, id, firstName, lastName, number, position, age, height, weight, college, salary):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.number = number
        self.position = position
        self.age = age
        self.height = height
        self.weight = weight
        self.college = college
        self.salary = salary

    @staticmethod
    def heightToMeters(value):
        value = re.sub(r"\s+", "", value)
        value = re.sub(r"\"", "", value)
        tokens = value.split("'")
        total = int(tokens[0])*12+int(tokens[1])
        meters = total*0.0254
        return meters
    
    @staticmethod
    def lbstoKilograms(arg):
        arg = re.sub(r"\D+", "", arg) # \D finds anything not (0-9)
        kilos = int(arg) * 0.45359237
        return kilos 
    
    def genURL(self):
        return "https://www.espn.com/nba/player/_/id/"+self.id+"/"+self.firstName.lower()+"-"+self.lastName.lower()


