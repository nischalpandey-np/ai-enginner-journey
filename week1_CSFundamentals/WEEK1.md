
# 🧠 Week 1: Computer Science Fundamentals

## Part 1: Data Representation & Binary Systems

### Bits and Bytes
- A **bit** (binary digit) is the smallest unit of data in computing. It can be either **0** or **1**.
- A **byte** = 8 bits.

#### Storage Units:
| Unit         | Size         |
|--------------|--------------|
| 1 bit        | 0 or 1       |
| 1 byte       | 8 bits       |
| 1 kilobyte   | 1024 bytes   |
| 1 megabyte   | 1024 KB      |

### Binary Number System
Binary is **base-2**, using only 0 and 1.

#### Example:
Binary `1011` = \( 1×2^3 + 0×2^2 + 1×2^1 + 1×2^0 = 11 \)

### Sorting Text and Numbers
- Strings sorted by ASCII/Unicode values.
- Numbers sorted numerically.
- Normalize data before sorting (e.g., lowercase conversion).

---

## Part 2: Basics of Computer Networks

### What is a Computer Network?
A collection of connected devices sharing data and resources.

### Types:
- **LAN**: Local Area Network
- **WAN**: Wide Area Network
- **MAN**: Metropolitan Area Network

### Key Devices:
- Router, Switch, Modem

### IP Addresses
- IPv4: `192.168.1.1`
- IPv6: `2001:0db8:85a3::8a2e:0370:7334`

### Routing Protocols
- **IP**: Internet Protocol
- **TCP/UDP**: Data transport
- **BGP**: Best path between networks

---

## Part 3: Network Communication Protocols & The World Wide Web

### TCP (Transmission Control Protocol)
- Reliable, ordered, error-checked.
- Slower but trustworthy.
- Used in HTTP, FTP, Emails.

### UDP (User Datagram Protocol)
- Fast, no guarantee of delivery.
- Used in video streaming, gaming.

### HTTP (HyperText Transfer Protocol)
- Used for loading web pages.
- Works on top of TCP.
- Stateless protocol.

### World Wide Web (WWW)
- A collection of interlinked web pages.
- Uses HTTP/HTTPS.
- Powered by browsers, servers, and URLs.

---

## Part 4: Programming Basics in Python

### Variables
```python
name = "Nischal"
age = 18
```

### Strings & Numbers
```python
greeting = "Hello"
print(greeting.upper())  # HELLO

x = 10
y = 3.14
print(x + y)
```

### Conditional Statements
```python
if age >= 18:
    print("Adult")
else:
    print("Minor")
```

### Loops
```python
for i in range(5):
    print(i)

count = 0
while count < 5:
    print(count)
    count += 1
```

---

## Part 5: Algorithm Basics

### What is an Algorithm?
A clear step-by-step method to solve a problem.

### Example: Add Two Numbers
```python
a = 5
b = 7
print("Sum:", a + b)
```

### Example: Find Largest of 3 Numbers
```python
if a >= b and a >= c:
    print(a)
```

### Good Algorithm Traits:
- Input, Output, Definiteness, Finiteness, Effectiveness

### Types of Algorithms:
- Sorting, Searching, Dynamic Programming, Backtracking, etc.

---
