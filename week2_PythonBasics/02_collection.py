# `list`, `tuple`, `set`, and `dictionary`.

## 🧺 Python Collections Overview

'''
| Type    | Ordered | Mutable | Allows Duplicates | Syntax      |
| ------- | ------- | ------- | ----------------- | ----------- |
| `list`  | ✅ Yes   | ✅ Yes   | ✅ Yes         | `[1, 2, 3]` |
| `tuple` | ✅ Yes   | ❌ No    | ✅ Yes         | `(1, 2, 3)` |
| `set`   | ❌ No    | ✅ Yes   | ❌ No          | `{1, 2, 3}` |
| `dict`  | ✅ Yes   | ✅ Yes   | ❌ Keys only   | `{"a": 1}`  |
'''

# ===== 1. LIST =====
print("🔹 List Demo")
fruits = ["apple", "banana", "mango"]
fruits.append("orange")
fruits.remove("banana")
print("List:", fruits)
print("Accessing 1st item:", fruits[0])
print()

# ===== 2. TUPLE =====
print("🔹 Tuple Demo")
point = (10, 20)
print("Tuple:", point)
print("Accessing x:", point[0])
# point[0] = 15  # ❌ Will raise error (tuples are immutable)
print()

# ===== 3. SET =====
print("🔹 Set Demo")
unique_nums = {1, 2, 3, 2, 1}
unique_nums.add(4)
unique_nums.discard(2)
print("Set (no duplicates, unordered):", unique_nums)
print()

# ===== 4. DICTIONARY =====
print("🔹 Dictionary Demo")
student = {
    "name": "Nischal",
    "age": 18,
    "skills": ["Python", "AI", "ML"]
}
student["age"] = 19
student["city"] = "butwal"
print("Dictionary:", student)
print("Student Name:", student["name"])
print("Student Skills:", ", ".join(student["skills"]))
print()

# ===== BONUS: Iterate all =====
print("🔹 Bonus: Looping Examples")

print("List loop:")
for fruit in fruits:
    print("-", fruit)

print("\nSet loop:")
for num in unique_nums:
    print("-", num)

print("\nDict loop:")
for key, value in student.items():
    print(f"{key}: {value}")



## ✅ Summary
'''
* Use **`list`** when order and duplicates matter.
* Use **`tuple`** for fixed, read-only data.
* Use **`set`** to store **unique** items only.
* Use **`dict`** to store data with a key-value pair.
'''