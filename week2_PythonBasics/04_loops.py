# Loops in Python

# ----------------------
# 1. For Loop
# ----------------------

print("For loop using range:")
for i in range(5):
    print(i)

print("\nFor loop over a string:")
for char in "Nischal":
    print(char)

# ----------------------
# 2. While Loop
# ----------------------

print("\nWhile loop example:")
count = 0
while count < 5:
    print(count)
    count += 1

# ----------------------
# 3. Break Statement
# ----------------------

print("\nBreak example in for loop:")
for i in range(10):
    if i == 5:
        break
    print(i)

# ----------------------
# 4. Continue Statement
# ----------------------

print("\nContinue example in for loop:")
for i in range(5):
    if i == 2:
        continue
    print(i)

# ----------------------
# 5. Else with Loop
# ----------------------

print("\nElse with for loop:")
for i in range(3):
    print(i)
else:
    print("Loop finished without break")

print("\nElse with break:")
for i in range(3):
    if i == 1:
        break
    print(i)
else:
    print("This will not print because of break")

# break and continue in Python
