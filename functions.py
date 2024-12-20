# Let's explore functions in Python

# Function definition
def greet(name):
    return f"Hello, {name}!"

# Function call
print(greet("Alice"))

# Function with default arguments
def greet_with_default(name="World"):
    return f"Hello, {name}!"

print(greet_with_default())
print(greet_with_default("Bob"))

# Function with variable number of arguments
def add(*args):
    return sum(args)

print(add(1, 2, 3))
print(add(4, 5))

# Function with keyword arguments
def introduce(name, age):
    return f"My name is {name} and I am {age} years old."

print(introduce(name="Alice", age=30))
print(introduce(age=25, name="Bob"))

# Lambda function
square = lambda x: x ** 2
print(square(5))
