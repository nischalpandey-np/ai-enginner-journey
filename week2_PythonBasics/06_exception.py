# ===========================================
# EXCEPTIONS IN PYTHON 
# ===========================================

# What are Exceptions?
# ---------------------
# Exceptions are errors that occur during the execution of a program.
# Instead of crashing, Python allows you to "handle" these errors gracefully using try-except blocks.

# ---------------------
# 1. Basic try-except
# ---------------------
print("1. Basic try-except:")

try:
    x = 5 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")

# ---------------------
# 2. Catching specific exceptions
# ---------------------
print("\n2. Catching specific exceptions:")

try:
    num = int("abc")  # invalid conversion
except ValueError:
    print("That's not a valid number!")

# ---------------------
# 3. Catching multiple exceptions
# ---------------------
print("\n3. Catching multiple exceptions:")

try:
    a = int("10")
    b = 10 / 0
except ValueError:
    print("Conversion failed.")
except ZeroDivisionError:
    print("Division by zero.")

# ---------------------
# 4. Using else with try-except
# ---------------------
print("\n4. Using else:")

try:
    num = int("100")
except ValueError:
    print("Invalid number")
else:
    print("Conversion successful:", num)

# ---------------------
# 5. Finally block (executes no matter what)
# ---------------------
print("\n5. Using finally:")

try:
    print("Trying something risky...")
    x = 1 / 1
except ZeroDivisionError:
    print("Math error")
finally:
    print("This will always run.")

# ---------------------
# 6. Raising your own exceptions
# ---------------------
print("\n6. Raising exceptions manually:")

def check_age(age):
    if age < 18:
        raise ValueError("You must be at least 18 years old.")
    else:
        print("You are eligible.")

try:
    check_age(16)
except ValueError as e:
    print("Caught Exception:", e)

# ---------------------
# 7. Custom Exception Class
# ---------------------
print("\n7. Custom Exception Class:")

class NegativeNumberError(Exception):
    pass

def square_root(x):
    if x < 0:
        raise NegativeNumberError("Cannot calculate square root of negative number.")
    else:
        return x ** 0.5

try:
    print(square_root(-4))
except NegativeNumberError as e:
    print("Custom Error:", e)

# ---------------------
# 8. Summary
# ---------------------
"""
Summary of keywords:
- try: Code that might cause an exception
- except: Code to handle the exception
- else: Runs if no exception occurs
- finally: Always runs, even if exception occurred
- raise: Manually trigger an exception
"""

# ===========================================
# End of Exceptions in Python
# ===========================================
