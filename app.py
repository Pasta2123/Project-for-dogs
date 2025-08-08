import random

class Pes:
    used_names = {}

    def __init__(self, gender, name, age):
        #if statement for two same dogs with same name
        if name in Pes.used_names:
            Pes.used_names[name] += 1
            name = f"{name}{Pes.used_names[name]}"
        else:
            Pes.used_names[name] = 1
        
        self.gender = gender
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name} is a {self.age}-year-old and is a {self.gender}"
    



pes1 = Pes("male", "Buddy", 3)
pes2 = Pes("female", "Courtney", 2)
pes3 = Pes("male", "Buddy", 4)  # This will create a new instance with a modified name
# Example usage
print(pes1)
print(pes2)
print(pes3)  # This will print "Buddy2 is a 4-year-old and        