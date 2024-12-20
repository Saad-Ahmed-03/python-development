# Let's explore string formatting in Python

# Using the old style '%' for string formatting
name = "Alice"
age = 30
print("Hello, %s. You are %d years old." % (name, age))

# Using the 'str.format()' method
print("Hello, {}. You are {} years old.".format(name, age))
print("Hello, {0}. You are {1} years old.".format(name, age))
print("Hello, {name}. You are {age} years old.".format(name=name, age=age))

# Using f-strings (formatted string literals) - Python 3.6+
print(f"Hello, {name}. You are {age} years old.")

# Formatting numbers
number = 123.456789
print("Formatted number: {:.2f}".format(number))  # 2 decimal places
print(f"Formatted number: {number:.2f}")          # 2 decimal places with f-string

# Padding and aligning strings
text = "Hello"
print(f"{text:>10}")  # Right align
print(f"{text:<10}")  # Left align
print(f"{text:^10}")  # Center align

# Using different format specifiers
binary = 42
print(f"Binary: {binary:b}")   # Binary format
print(f"Hex: {binary:x}")      # Hexadecimal format
print(f"Octal: {binary:o}")    # Octal format