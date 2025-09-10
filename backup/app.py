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
    while True:

        gender = input("Please enter the dog's gender: ").strip().lower()
        if gender not in ("Female", "female", "Male", "male"):
            print("please enter correct syntax")
        else:
            break
        
    name = input("Please enter the dog's name: ").strip()
        
    while True:
        try:
            age = int(input("Please enter the dog's age: ").strip())
            if age > 20 or age < 0:
                print("Please enter a valid age between 0 and 20.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")
    return Dog(gender, name, age)

def print_available_doghouses():
    print("\nAvailable Doghouses:")
    # Combine all doghouses into one list and filter only those without dogs
    available_houses = []
    for house in doghouses:
        if not house.dogs:
            available_houses.append(house)
    for house in doghouses_with_paddock:
        if not house.dogs:
            available_houses.append(house)

    if not available_houses:
        print("No doghouses available.")
        return []

    for i, house in enumerate(available_houses, start=1):
        if isinstance(house, Doghouse_with_paddock):
            print(f"{i}. Doghouse with paddock - {house.size} ({house.color}), paddock size: {house.paddock_size}")
        else:
            print(f"{i}. Doghouse - {house.size} ({house.color})")
    return available_houses

# User input for each their dog to be added to Doghouse or Doghouse_with_paddock
def assign_doghouse(dog):
    while True:
        available_houses = print_available_doghouses()
        if not available_houses:
            print("No available doghouses left!")
            return
        try:
            choice = int(input(f"\nWhich doghouse would you like to assign to {dog.name}? (number): "))
            if 1 <= choice <= len(available_houses):
                selected_house = available_houses[choice - 1]
                selected_house.add_dog(dog)
                print(f"{dog.name} has been assigned to {selected_house.info()}")
                break
            else:
                print("Invalid choice. Please try again.")
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





