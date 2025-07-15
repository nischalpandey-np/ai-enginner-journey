
---

## 🧠 Week 1: Computer Science Fundamentals

### 📌 Topics Covered:

* Data Representation

  * Bits & Bytes
  * Sorting Text and Numbers
  * Binary Number System

---

### 🧮 1. Bits and Bytes

* A **bit** (binary digit) is the smallest unit of data in computing. It can be either **0** or **1**.
* A **byte** = 8 bits.
  Example: `01000001` → represents the letter **A** in ASCII.

| Storage Unit | Size       |
| ------------ | ---------- |
| 1 bit        | 0 or 1     |
| 1 byte       | 8 bits     |
| 1 kilobyte   | 1024 bytes |
| 1 megabyte   | 1024 KB    |
| ...          | ...        |

🔍 Fun fact: The image you see or the text you read on a screen is just a series of 0s and 1s behind the scenes!

---

### 🔢 2. Binary Number System

* Binary is **base-2**, using only 0 and 1.
* Each binary digit represents a power of 2.

#### Example:

Binary `1011`
\= $(1 \times 2^3) + (0 \times 2^2) + (1 \times 2^1) + (1 \times 2^0)$
\= $8 + 0 + 2 + 1 = 11$

| Binary | Decimal |
| ------ | ------- |
| 0001   | 1       |
| 0010   | 2       |
| 0100   | 4       |
| 1000   | 8       |

📌 Binary is used for:

* CPU instructions
* Network protocols
* Low-level programming (Assembly, Machine Code)

---

### 📄 3. Sorting Text and Numbers

#### Sorting Text (Strings)

* Computers sort text using **ASCII** or **Unicode** values.
* Example:

  * `"Apple"` comes before `"banana"` because uppercase letters have lower ASCII values than lowercase.

#### Sorting Numbers

* Works as expected: numerically from lowest to highest (or reverse).
* Caution: In some languages, `"10"` (as a string) comes before `"2"` because it sorts alphabetically.

| Input (Strings)       | Sorted Output         |
| --------------------- | --------------------- |
| "cat", "Dog", "apple" | "Dog", "apple", "cat" |

🛠️ Tip: Always normalize data before sorting (e.g., convert to lowercase for string sorting).

---

### ✅ Summary

| Concept         | Key Point                                   |
| --------------- | ------------------------------------------- |
| Bit             | Smallest unit of data (0 or 1)              |
| Byte            | 8 bits                                      |
| Binary Number   | Base-2 number system                        |
| Sorting Text    | Based on character encoding (ASCII/Unicode) |
| Sorting Numbers | Numeric comparison                          |

---
