# ============= STRINGS IN PYTHON =============

# 1. String Creation
s1 = "Hello"
s2 = 'World'
s3 = '''This is 
a multiline string.'''

print("s1:", s1)
print("s2:", s2)
print("s3:", s3)

# 2. Indexing and Slicing
text = "icecream"
print("\nOriginal text:", text)
print("First character:", text[0])         # i
print("Last character:", text[-1])         # m
print("Slice [2:5]:", text[2:5])           # ecr
print("Reverse:", text[::-1])              # maerceci

# 3. String Methods
s = " Hello World "
print("\nOriginal:", repr(s))
print("strip():", s.strip())               # Removes whitespace
print("lower():", s.lower())
print("upper():", s.upper())
print("title():", s.title())
print("replace():", s.replace("World", "Python"))
print("split():", s.split())               # ['Hello', 'World']
print("join():", "-".join(["A", "B", "C"]))  # A-B-C
print("find():", s.find("World"))          # Returns index of 'World'

# 4. String Testing Methods
s2 = "hello123"
print("\nString:", s2)
print("isalpha():", s2.isalpha())          # False
print("isdigit():", s2.isdigit())          # False
print("isalnum():", s2.isalnum())          # True
print("isspace():", s2.isspace())          # False

# 5. String Formatting
name = "Nischal"
age = 20
print("\nString Formatting:")
print(f"My name is {name} and I am {age} years old.")  # f-string
print("My name is {} and I am {} years old.".format(name, age))  # .format()

# 6. Escape Characters
print("\nEscape Characters:")
print("He said, \"Hello!\"")
print("Line1\nLine2")
print("C:\\Users\\name")

# 7. Length of String
print("\nLength of 'icecream':", len(text))

# 8. Check Substring
print("\nSubstring Check:")
print("'cream' in 'icecream':", "cream" in text)
print("'cake' not in 'icecream':", "cake" not in text)

# 9. String Immutability
print("\nImmutability Example:")
s = "hello"
# s[0] = "H"  ❌ This will raise an error
s = "Hello"  # ✅ This is allowed
print("Modified string:", s)
