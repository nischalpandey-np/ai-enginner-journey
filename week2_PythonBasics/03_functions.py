# ============================
# Functions in Python
# ============================

# 1. Simple function without parameters
def greet():
    print("Hello, welcome to Python!")

greet()


# 3. Function with return value
def add(a, b):
    return a + b

result = add(5, 3)
print("Sum is:", result)

# 4. Function with default parameter
def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Nischal")

# 5. Function returning multiple values
def calculator(a, b):
    return a + b, a - b, a * b, a / b

addition, sub, mul, div = calculator(10, 2)
print("Add:", addition)
print("Subtract:", sub)
print("Multiply:", mul)
print("Divide:", div)

# 6. Using function inside a loop
def square(num):
    return num * num

for i in range(5):
    print("Square of", i, "is", square(i))

# ============================
# Lambda Functions in Python
# ============================

# A lambda function is an anonymous function — used for short, simple operations
# Syntax: lambda arguments: expression

# 1. Lambda for addition
add = lambda a, b: a + b
print("Lambda Add:", add(3, 7))

# 2. Lambda to square a number
square = lambda x: x * x
print("Lambda Square of 4:", square(4))

# 3. Lambda inside a sort function (sorting by length of string)
names = ["Nischal", "AI", "Python", "Nepal"]
names.sort(key=lambda name: len(name))
print("Sorted by length:", names)

# 4. Lambda with map() - apply function to all items in a list
nums = [1, 2, 3, 4]
squares = list(map(lambda x: x ** 2, nums))
print("Squares using map + lambda:", squares)

# 5. Lambda with filter() - filter items in a list
even = list(filter(lambda x: x % 2 == 0, nums))
print("Even numbers using filter + lambda:", even)


# ======================================================

tomExp=[234,234,23,43]
joeExp=[239,33,23,115]

# create a function to calculate sum of each ... 

def calculateTotal(exp):
    total = 0
    for item in exp:
        total=total + item
    return total

tomsTotal = calculateTotal(tomExp)
joesTotal=calculateTotal(joeExp)
print(f"Tom's Total is {tomsTotal}")
print(f"Joe's Total is {joesTotal}")
