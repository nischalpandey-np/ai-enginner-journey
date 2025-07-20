# ===========================================
# FILE HANDLING IN PYTHON 
# ===========================================

# Python allows you to work with files using built-in functions like open(), read(), write(), etc.

# File Modes:
# ---------
# 'r'  - read (default)
# 'w'  - write (overwrites file)
# 'a'  - append (adds to end)
# 'x'  - create (fails if file exists)
# 'b'  - binary mode (e.g., 'rb' or 'wb')
# 't'  - text mode (default)

# -------------------------
# 1. Writing to a File
# -------------------------
print("1. Writing to a file")

with open("example.txt", "w") as file:
    file.write("Hello, world!\n")
    file.write("This is Python file handling.\n")

print("✅ File 'example.txt' created and written.")

# -------------------------
# 2. Reading a File
# -------------------------
print("\n2. Reading from the file")

with open("example.txt", "r") as file:
    content = file.read()
    print("📄 File content:\n", content)

# -------------------------
# 3. Reading Line by Line
# -------------------------
print("\n3. Reading line by line")

with open("example.txt", "r") as file:
    for line in file:
        print("👉", line.strip())

# -------------------------
# 4. Appending to a File
# -------------------------
print("\n4. Appending to the file")

with open("example.txt", "a") as file:
    file.write("Appending a new line.\n")

# Let's check the updated content
with open("example.txt", "r") as file:
    print("📄 Updated File:\n", file.read())

# -------------------------
# 5. File Existence Check (Optional)
# -------------------------
print("\n5. Checking if a file exists")

import os
if os.path.exists("example.txt"):
    print("✅ example.txt exists")
else:
    print("❌ File not found")

# -------------------------
# 6. Deleting a File (Optional)
# -------------------------
# Uncomment the lines below to delete the file

# if os.path.exists("example.txt"):
#     os.remove("example.txt")
#     print("🗑️ File deleted.")
# else:
#     print("File not found.")

# -------------------------
# 7. Try-Except for Safety
# -------------------------
print("\n6. Handling file errors")

try:
    with open("missing.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("⚠️ The file does not exist.")

# ===========================================
# End of File Handling in Python
# ===========================================


# Manual way to open file (not recommended)

file = open("example.txt", "r")
content = file.read()
print(content)
file.close()  # You must remember to close the file

