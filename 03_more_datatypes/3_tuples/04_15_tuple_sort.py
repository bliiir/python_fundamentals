'''
Write a script that sorts a list of tuples based on the number value in the tuple.
For example:

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = [('second_element', 2), ('first_element', 4), ('third_element', 6)]
'''


# Long version ---------------------------------------------------------
unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]

def sort_key(n):
    '''Return the second element of the tuple'''
    
    return n[1]   

def sort_list(unsorted_list): 
    '''Use the sorted command to sort the list of tuples 
    using the sort_key function as the key'''
    
    # Create a sorted list using the sort_key function as the key
    sorted_list = sorted(unsorted_list, key = sort_key) 
    
    return sorted_list

# Call the sort function on the unsorted list and store the returned value 
# in a variable called sorted_list
sorted_list = sort_list(unsorted_list)

# Print the result to the console
print(sorted_list)


# Shorter version ------------------------------------------------------
unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]

def sort_key(n):
    return n[1] 

sorted_list = sorted(unsorted_list, key = sort_key)
print(sorted_list)


# Short version --------------------------------------------------------

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = sorted(unsorted_list, key=lambda element: element[1])
print(sorted_list)