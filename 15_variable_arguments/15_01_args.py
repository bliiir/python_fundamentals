'''
Write a script with a function that demonstrates the use of *args.

'''

def my_args(*args):
    '''Print out the arguments received
    '''
    print('These are the arguments you gave me: \n')
    for arg in args:
        print(arg)

# Call the my_args function with a string, a number and a copy of itself
unsure('a string', 4, my_args)
