# Let's explore lists in Python

# List creation
fruits = ["apple", "banana", "cherry"]
print("List of fruits:", fruits)

# Accessing list elements
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# List slicing
print("First two fruits:", fruits[:2])

# Adding elements to a list
fruits.append("orange")
print("After appending:", fruits)

# Inserting elements into a list
fruits.insert(1, "blueberry")
print("After inserting:", fruits)

# Removing elements from a list
fruits.remove("banana")
print("After removing:", fruits)

# Popping elements from a list
popped_fruit = fruits.pop()
print("Popped fruit:", popped_fruit)
print("After popping:", fruits)

# List comprehension
squares = [x * x for x in range(5)]
print("List of squares:", squares)
