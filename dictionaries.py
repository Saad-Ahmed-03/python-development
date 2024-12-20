def dictionary_operations():
    # Create a dictionary
    my_dict = {
        'a': 1, 
        'b': 2, 
        'c': 3
        }
    print("Original dictionary:", my_dict)
    
    # Access elements
    print("Value for key 'a':", my_dict['a'])
    
    # Add an element
    my_dict['d'] = 4
    print("Dictionary after adding an element:", my_dict)
    
    # Remove an element
    del my_dict['b']
    print("Dictionary after removing an element:", my_dict)
    
    # Get all keys
    print("Keys in dictionary:", list(my_dict.keys()))
    
    # Get all values
    print("Values in dictionary:", list(my_dict.values()))

# Call the function to demonstrate dictionary operations
dictionary_operations()
