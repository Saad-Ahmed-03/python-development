# Let's dive into the variables and data types in Python

# Initialization of variables:
print("Initialization of variables:")
int_num1 = 10
int_num2 = 5
float_num1 = 15.55
float_num2 = 10.65
string1 = "Hello"
string2 = "World"

# Printing the variables
print("Printing the variables:")
print(int_num1)
print(int_num2)
print(float_num1)
print(float_num2)
print(string1)
print(string2)

# Printing the type of variables
print("Printing the type of variables:")
print(type(int_num1))
print(type(int_num2))
print(type(float_num1))
print(type(float_num2))
print(type(string1))
print(type(string2))

# Problem #1: Write a program to add/subtract/multiply/divide two numbers with int and float data types and print the result.

print("Writing a program with int data type:")

int_sum = int_num1 + int_num2  # Initialization of sum variable and perform addition operation
print("Sum:", int_sum)  # Printing the sum

int_subtract = int_num1 - int_num2  # Initialization of subtract variable and perform subtraction operation
print("Subtract:", int_subtract)  # Printing the subtract

int_multiply = int_num1 * int_num2  # Initialization of multiply variable and perform multiplication operation
print("Multiply:", int_multiply)  # Printing the multiply

int_divide = int_num1 / int_num2  # Initialization of divide variable and perform division operation
print("Divide:", int_divide)  # Printing the divide

print("Writing a program with float data type:")

float_sum = float_num1 + float_num2  # Initialization of sum variable and perform addition operation
print("Sum:", float_sum)  # Printing the sum

float_subtract = float_num1 - float_num2  # Initialization of subtract variable and perform subtraction operation
print("Subtract:", float_subtract)  # Printing the subtract

float_multiply = float_num1 * float_num2  # Initialization of multiply variable and perform multiplication operation
print("Multiply:", float_multiply)  # Printing the multiply

float_divide = float_num1 / float_num2  # Initialization of divide variable and perform division operation
print("Divide:", float_divide)  # Printing the divide

# Problem #2: Write a program to add two numbers taking the input from the user & perform arithmetic operations (+, -, *, /) on the two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

sum_result = num1 + num2
subtract_result = num1 - num2
multiply_result = num1 * num2
divide_result = num1 / num2

print("The sum of {0} and {1} is {2}".format(num1, num2, sum_result))
print("The subtraction of {0} and {1} is {2}".format(num1, num2, subtract_result))
print("The multiplication of {0} and {1} is {2}".format(num1, num2, multiply_result))
print("The division of {0} and {1} is {2}".format(num1, num2, divide_result))