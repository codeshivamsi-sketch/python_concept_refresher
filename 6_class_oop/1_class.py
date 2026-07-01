class Dog:
    def __init__(self, name, age): # runs when object is created
        self.name = name
        self.age = age
    
    def bark(self):
        print(f"{self.name} says woof!")




# Create dog objects
dog1 = Dog("Raju", 3)
dog2 = Dog("Max", 2)

dog1.bark()
print(dog2.name)

