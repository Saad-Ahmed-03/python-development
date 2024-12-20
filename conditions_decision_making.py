# Let's explore conditions and decision making in Python

# If statement
num = 10
if num > 0:
    print(f"{num} is a positive number.")

# If-else statement
num = -5
if num >= 0:
    print(f"{num} is a positive number.")
else:
    print(f"{num} is a negative number.")

# If-elif-else statement
num = 0
if num > 0:
    print(f"{num} is a positive number.")
elif num == 0:
    print(f"{num} is zero.")
else:
    print(f"{num} is a negative number.")

# Nested if statement
num = 10
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")

# One-liner if statement
num = 10
print(f"{num} is positive.") if num > 0 else print(f"{num} is negative or zero.")