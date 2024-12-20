# Let's explore basic string operations in Python

# String concatenation
str1 = "Hello"
str2 = "World"
concatenated = str1 + " " + str2
print("Concatenated string:", concatenated)

# String repetition
repeated = str1 * 3
print("Repeated string:", repeated)

# String slicing
sliced = concatenated[0:5]
print("Sliced string:", sliced)

# String length
length = len(concatenated)
print("Length of string:", length)

# String case conversion
upper_case = concatenated.upper()
lower_case = concatenated.lower()
print("Upper case:", upper_case)
print("Lower case:", lower_case)

# String stripping
whitespace_str = "   Hello World   "
stripped = whitespace_str.strip()
print("Stripped string:", stripped)

# String splitting
split_str = concatenated.split(" ")
print("Split string:", split_str)

# String joining
joined_str = "-".join(split_str)
print("Joined string:", joined_str)

# String find
find_index = concatenated.find("World")
print("Index of 'World':", find_index)

# String replace
replaced_str = concatenated.replace("World", "Python")
print("Replaced string:", replaced_str)