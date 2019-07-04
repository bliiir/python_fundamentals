'''
Write a script with a function that demonstrates the use of **kwargs.

'''

def my_kwargs(**kwargs):
    '''Print out the arguments received
    '''
    print('\nThese are the arguments you gave me: \n')
    print('First as a dictionary: ', kwargs)
    print('\nThen individually:\n')
    for k, v in kwargs.items():
        print(f'{k:<15s}: {v:}')

# Call the my_args function with a string, a number and a copy of itself
my_kwargs(
    my_string='Hello!', 
    my_number=4, 
    my_list=[1,2,4], 
    my_function=my_kwargs)