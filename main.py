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
