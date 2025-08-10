import random

class Dog:
    used_names = {}

    def __init__(self, gender, name, age, location=None):
        
        #if statement for two same dogs with same name
        if name in Dog.used_names:
            Dog.used_names[name] += 1
            name = f"{name}{Dog.used_names[name]}"
        else:
            Dog.used_names[name] = 1
        
        self.gender = gender
        self.name = name
        self.age = age
        self.location = None
    
    def __str__(self):
        location_info = "no location"
        if self.location:
            location_info = self.location.info()
        return f"{self.name} is a {self.age}-year-old and is a {self.gender}. Location: {location_info}"
    
class Doghouse:
    def __init__(self, color, size):
        self.color = color
        self.size = size
        self.dogs = []
    
    def add_dog(self, dog):
        self.dogs.append(dog)
        dog.location = self
    
    def info(self):
        return f"a {self.color} doghouse of size {self.size}."
        
        

class Doghouse_with_paddock(Doghouse):
    def __init__(self, color, size, paddock_size):
        super().__init__(color, size)
        self.paddock = True
        self.paddock_size = paddock_size
    
    def info(self):
        return f"a {self.color} doghouse with a paddock of size {self.paddock_size}."



dog1 = Dog("male", "Buddy", 3)
dog2 = Dog("female", "Courtney", 2)
dog3 = Dog("male", "Buddy", 4)  # This will create a new instance with a modified name

doghouse = Doghouse("brown", "Small")
doghouse.add_dog(dog1)

doghouse_with_paddock = Doghouse_with_paddock("Yellow", "Small", "Large")
doghouse_with_paddock.add_dog(dog2)


# Example usage
print(dog1)
print(dog2)
print(dog3)  # This will print "Buddy2 is a 4-year-old and        