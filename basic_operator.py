# Let's explore basic operators in Python

# Arithmetic Operators
print("Arithmetic Operators:")
a = 10
b = 5

print("Addition:", a + b)        # Addition
print("Subtraction:", a - b)     # Subtraction
print("Multiplication:", a * b)  # Multiplication
print("Division:", a / b)        # Division
print("Modulus:", a % b)         # Modulus
print("Exponent:", a ** b)       # Exponentiation
print("Floor Division:", a // b) # Floor Division

# Comparison Operators
print("\nComparison Operators:")
print("Equal:", a == b)          # Equal
print("Not Equal:", a != b)      # Not Equal
print("Greater than:", a > b)    # Greater than
print("Less than:", a < b)       # Less than
print("Greater than or equal to:", a >= b) # Greater than or equal to
print("Less than or equal to:", a <= b)    # Less than or equal to

# Logical Operators
print("\nLogical Operators:")
x = True
y = False

print("AND:", x and y)           # AND
print("OR:", x or y)             # OR
print("NOT:", not x)             # NOT

# Bitwise Operators
print("\nBitwise Operators:")
c = 6  # 110 in binary
d = 2  # 010 in binary

print("AND:", c & d)             # AND
print("OR:", c | d)              # OR
print("XOR:", c ^ d)             # XOR
print("NOT:", ~c)                # NOT
print("Left Shift:", c << 1)     # Left Shift
print("Right Shift:", c >> 1)    # Right Shift

# Assignment Operators
print("\nAssignment Operators:")
e = 10

e += 5
print("Add and assign:", e)      # Add and assign

e -= 3
print("Subtract and assign:", e) # Subtract and assign

e *= 2
print("Multiply and assign:", e) # Multiply and assign

e /= 4
print("Divide and assign:", e)   # Divide and assign

e %= 3
print("Modulus and assign:", e)  # Modulus and assign

e **= 2
print("Exponent and assign:", e) # Exponent and assign

e //= 2
print("Floor divide and assign:", e) # Floor divide and assign