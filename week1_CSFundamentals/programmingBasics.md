
---

## 🧠 Week 1 (Part 4): Programming Basics in Python

### 📌 Topics Covered:

* Variables
* Strings & Numbers
* Conditional Statements (`if`)
* Loops (`for`, `while`)

---

### 🧱 1. Variables

A **variable** is like a labeled box that stores a value in memory.

```python
name = "Nischal"
age = 18
```

* Variables store **strings**, **numbers**, **lists**, etc.
* You can change the value anytime.

```python
name = "Aashma"  # Reassigned value
```

---

### 🔤 2. Strings & Numbers

#### Strings

Textual data enclosed in quotes.

```python
greeting = "Hello, World!"
print(greeting.lower())     # hello, world!
print(greeting.upper())     # HELLO, WORLD!
print(len(greeting))        # 13
```

#### Numbers

Can be integers or floats.

```python
x = 10        # Integer
y = 3.14      # Float

print(x + y)  # 13.14
```

🧠 Tip: You can’t mix types directly (e.g., add string + int) without conversion.

```python
name = "Nischal"
age = 18
print(name + str(age))  # Nischal18
```

---

### 🤔 3. Conditional Statements (`if`)

Used to make decisions in your code.

```python
age = 18

if age >= 18:
    print("You're an adult")
else:
    print("You're a minor")
```

#### 🧱 if-elif-else structure:

```python
num = 0

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
```

---

### 🔁 4. Loops

Loops help you **repeat** tasks.

#### `for` loop

Used for iterating over sequences (like lists or strings).

```python
for i in range(5):
    print(i)  # 0 1 2 3 4
```

#### `while` loop

Runs **as long as** a condition is true.

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

---

### ✅ Summary

| Concept    | Example              | Use Case                         |
| ---------- | -------------------- | -------------------------------- |
| Variables  | `name = "Nischal"`   | Store data                       |
| Strings    | `"hello".upper()`    | Text manipulation                |
| Numbers    | `x = 10 + 5.2`       | Math operations                  |
| if/else    | `if age > 18:`       | Decision-making                  |
| for loop   | `for i in range(5):` | Iterating over a sequence        |
| while loop | `while x < 10:`      | Repeating tasks with a condition |

---
