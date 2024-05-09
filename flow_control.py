# 1. To what values do the following expressions evaluate?
False or (True and False)   # False
True or (1 + 2)             # True
(1 + 2) or True             # 3
True and (1 + 2)            # 3
False and (1 + 2)           # False
(1 + 2) and True            # True
(32 * 4) >= 129             # True
False != (not True)         # False
True == 4                   # False
False == (847 == '847')     # True

# 2. Write a function, 'even_or_odd', that determines whether its argument is
# an even or odd number. If it's even, the function should print 'even';
# otherwise, it should print 'odd'. Assume the argument is always an integer.
def even_or_odd(number):
    if number % 2 == 0:
        print('even')
    else:
        print('odd')

# 3. Without running the following code, what does it print? Why?
def bar_code_scanner(serial):
    match serial:
        case '123':
            print('Product1')
        case '113':
            print('Product2')
        case '142':
            print('Product3')
        case _:
            print('Product not found!')

bar_code_scanner('113')
bar_code_scanner(142)
'''
The first function call prints out 'Product2'. However, the second function
call prints out 'Product not found!'
'''

# 4. Refactor this statement to use a regular 'if' statement instead.
return ('bar' if foo() else qux())

# Rearranged function:
if foo():
    return 'bar'
else:
    return qux()

# 5. What does this code output, and why?
def is_list_empty(my_list):
    if my_list:
        print('Not Empty')
    else:
        print('Empty')

is_list_empty([])
'''
The code outputs 'Empty' because the list used as an argument is empty. This
means that the 'else' block will run instead of the 'if' block.
'''

# 6. Write a function that takes a string as an argument and returns an
# all-caps version of the string when the string is longer than 10 characters.
# Otherwise, it should return the original string
def capitalize(phrase):
    if len(phrase) > 10:
        return phrase.upper()
    else:
        return phrase
    
# 7. Write a function that takes a single integer argument and prints a message
# that describes whether:
# the value is between 0 and 50 (inclusive)
# the value is between 51 and 100 (inclusive)
# the value is greater than 100
# the value is less than 0
def number_range(number):
    if number >= 0 and number <= 50:
        print(f'{number} is between 0 and 50')
    elif number >= 51 and number <= 100:
        print(f'{number} is between 51 and 100')
    elif number > 100:
        print(f'{number} is greater than 100')
    else:
        print(f'{number} is less than 0')