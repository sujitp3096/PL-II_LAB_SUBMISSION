# Single Inheritance Example
class Animal:
    def sound(self):
        print("Animals make sound")

class Dog(Animal):  # Single inheritance
    def bark(self):
        print("Dog barks: Woof!")

print("== Single Inheritance ==")
dog = Dog()
dog.sound()  # Inherited from Animal
dog.bark()   # Own method
print()

# Multiple Inheritance Example
class Father:
    def skills(self):
        print("Father: Gardening and Cooking")

class Mother:
    def skills(self):
        print("Mother: Painting and Singing")

class Child(Father, Mother):  # Multiple inheritance
    def skills(self):
        print("Child: Sports")
        print("Also inherits skills from parents:")
        Father.skills(self)
        Mother.skills(self)

print("== Multiple Inheritance ==")
child = Child()
child.skills()