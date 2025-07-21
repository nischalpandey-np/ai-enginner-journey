# ========================================
# OOP IN PYTHON - Week 2 Final Boss 🐍👑
# ========================================

# ----------------------------------------
# 1. What is OOP?
# ----------------------------------------
# Object-Oriented Programming is a way to structure code using:
# - Classes (blueprints)
# - Objects (real-world instances)
# - Key concepts: Encapsulation, Inheritance, Polymorphism, Abstraction

# ----------------------------------------
# 2. Creating a Class and Object
# ----------------------------------------

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says woof!")

# Creating object
dog1 = Dog("Buddy", "Golden Retriever")
dog1.bark()  # Output: Buddy says woof!

# ----------------------------------------
# 3. Class vs Object
# ----------------------------------------
# Dog = Class (Blueprint)
# dog1 = Object (Instance of Dog class)

# ----------------------------------------
# 4. Encapsulation
# ----------------------------------------
# Keeping data safe inside the class

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print("Balance:", account.get_balance())  # ✅ Safe access

# ----------------------------------------
# 5. Inheritance
# ----------------------------------------
# One class inherits features from another

class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        print("Some sound")

class Cat(Animal):
    def __init__(self, name):
        super().__init__("Cat")
        self.name = name

    def make_sound(self):
        print("Meow!")

cat1 = Cat("Whiskers")
cat1.make_sound()  # Output: Meow!

# ----------------------------------------
# 6. Polymorphism
# ----------------------------------------
# Same method, different behaviors

class Bird:
    def speak(self):
        print("Chirp")

class Human:
    def speak(self):
        print("Hello")

def make_speak(entity):
    entity.speak()

make_speak(Bird())   # Chirp
make_speak(Human())  # Hello

# ----------------------------------------
# 7. Abstraction (using abc module)
# ----------------------------------------

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

r = Rectangle(4, 5)
print("Area of Rectangle:", r.area())

# ========================================
# BONUS: __str__() method
# ========================================
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

b = Book("Atomic Habits", "James Clear")
print(b)  # Atomic Habits by James Clear

# ========================================
# END OF OOP IN PYTHON ✅
# ========================================
