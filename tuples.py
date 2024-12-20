def tuple_operations():
    # Create a tuple
    my_tuple = (1, 2, 3, 4, 5)
    print("Original tuple:", my_tuple)
    
    # Access elements
    print("First element:", my_tuple[0])
    print("Last element:", my_tuple[-1])
    
    # Slicing
    print("Sliced tuple (2nd to 4th):", my_tuple[1:4])
    
    # Concatenation
    new_tuple = my_tuple + (6, 7)
    print("Concatenated tuple:", new_tuple)
    
    # Tuple length
    print("Length of tuple:", len(my_tuple))

# Call the function to demonstrate tuple operations
tuple_operations()
