class Animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")


class Dog(Animal): # Dog interits from Animal
    def speak(self): # Overrides parents's speak
        print(f"{self.name} barks")


class Cat(Animal):
    def seak(self):
        print(f"{self.name} mewos")


dog = Dog("Raju")
cat = Dog("Tom")

dog.speak()
cat.speak()