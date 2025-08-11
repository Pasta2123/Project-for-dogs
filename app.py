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

doghouses = [
    Doghouse("brown", "Small"),
    Doghouse("white", "Medium"),
    Doghouse("red", "Large"),
    Doghouse("yellow", "Small"),
    Doghouse("blue", "Medium"),
]

doghouses_with_paddock = [
    Doghouse_with_paddock("green", "Small", "Large"),
    Doghouse_with_paddock("green", "Small", "Medium"),
    Doghouse_with_paddock("green", "Small", "Small"),
    Doghouse_with_paddock("green", "Small", "Large"),
    Doghouse_with_paddock("green", "Small", "Medium"),
]

# user input for dog
def get_dog_input():
    print("\nEnter dog details:")
    gender = input("Please enter the dog's gender: ").strip().lower()
    name = input("Please enter the dog's name: ").strip()
    age = int(input("Please enter the dog's age: ").strip())
    return Dog(gender, name, age)

def print_available_doghouses():
    print("\nAvailable Doghouses:")
    for i, doghouse in enumerate(doghouses, start=1):
        print(f"{i}. Doghouse - {doghouse.size} ({doghouse.color})")
    for i, doghouse in enumerate(doghouses_with_paddock, start=len(doghouses) + 1):
        print(f"{i}. Doghouse with paddock - {doghouse.size} ({doghouse.color})")



# User input for each their dog to be added to Doghouse or Doghouse_with_paddock
def assign_doghouse(dog):
    print_available_doghouses()
    while True:
        try:
            choice = int(input(f"\nWhich doghouse would you like to assign to {dog.name}? (number): "))
            if choice < 1 or choice > len(doghouses) + len(doghouses_with_paddock):
                print("Invalid choice. Please try again.")
            elif choice <= len(doghouses):
                selected_house = doghouses[choice - 1]
                if selected_house.dogs:
                    print("This doghouse already has a dog. Please choose another one.")
                    continue
                selected_house.add_dog(dog)
                print(f"{dog.name} has been assigned to a {selected_house.info()}")
                break
            else:
                selected_house = doghouses_with_paddock[choice - len(doghouses) - 1]
                if selected_house.dogs:
                    print("This doghouse already has a dog. Please choose another one.")
                    continue
                selected_house.add_dog(dog)
                print(f"{dog.name} has been assigned to a {selected_house.info()}")
                break
        except ValueError:
            print("Invalid input. Please enter a number.")
 





def main():
    dogs = [] 
    for i in range(10):
        choice = input("\nDo you want to add a dog? (yes/no): ").strip().lower()
        if choice in ("no", "n"):
            break
    
        new_dog = get_dog_input()
        dogs.append(new_dog)
        assign_doghouse(new_dog)

    print("\nAll dogs in the system:")
    for dog in dogs:
        print(dog)
if __name__ == "__main__":
    main()

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