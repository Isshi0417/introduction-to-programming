# 1. What happens when you run the following program? Why do we get that
# result?
def set_foo():
    foo = 'bar'

set_foo()
print(foo)
'''
set_foo() successfully assigns the value 'bar' to the variable 'foo'.
However, printing 'foo' will result in an error because 'foo' is a local
variable that only exists while the function is called.
'''

# 2. Take a look at this code snippet:
foo = 'bar'

def set_foo():
    foo = 'qux'

set_foo()
print(foo)
# What does this program print? Why?
'''
The program will print 'bar'. This is because the function creates a local 
variable and assigns the value to the newly created variable, which means that
the value of 'foo' outside the function is not changed.
'''

# 3. Write a program that uses a 'multiply' function to multiply the two
# numbers and returns the result. Ask the user to enter the two numbers, then
# output the numbers and result as a simple equation.
def multiply():
    a = input('Enter the first number: ')
    b = input('Enter the second number: ')
    print(f'{a} * {b} = {float(a) * float(b)}')

# 4. Consider this code:
def multiply_numbers(num1, num2, num3):
    result = num1 * num2 * num3
    return result

product = multiply_numbers(2, 3, 4)
# Identify the following items in that code:
'''
function name:          multiply_numbers on line 38 and 42
function arguments:     2, 3, 4 on line 42
function definition:    lines 35 to 40
function body:          line 39 and line 40
function parameter:     num1, num2, num3 on line 38
function invocation:    multiply_numbers(2, 3, 4) on line 42
function return value:  return result on line 40
all identifiers:        multiply_numbers, num1, num2, num3, result, and product
'''

# 5. What does the following code print?
def scream(words):
    return words + '!!!!'

scream('Yipeee')
'''
The code prints nothing because the function returns the value instead of
printing it.
'''

# 6. What does the following code print?
def scream(words):
    words = words + '!!!!'
    return
    print(words)

scream('Yipeee')
'''
The code prints nothing because the function terminates itself after return
'''

# 7. Without running the following code, what do you think it will do?
def foo(bar, qux):
    print(bar)
    print(qux)

foo('Hello')
'''
The code will result in an error because function 'foo' is defined with two 
parameters, but the function is called with only one argument.
'''

# 8. Without running the following code, what do you think it will do?
def foo(bar, qux):
    print(bar)
    print(qux)

foo(42, 3.141592, 2.718)
'''
The code will result in an error because function 'foo' is defined with two
parameters, but the function is called with three arguments.
'''

# 9. Without running the code, what do you think it will do?
def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42, 3.141592, 2.718)
'''
The code will print 42, 3.141592, and 2.718 respectively in their own lines.
'''

# 10. Without running the following code, what do you think it will do?
def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42, 3.141592)
'''
The code will print 42, 3.141592, and 2 respectively in their own lines.
'''

# 11. Without running the following code, what do you think it will do?
def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42)
'''
The code will print 42, 3, and 2 respectively in their own lines.
'''

# 12. Without running the following code, what do you think it will do?
def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo()
'''
The code will result in an error because the parameter, 'first', is not
assigned a default value.
'''

# 13. Without running the following code, what do you think it will do?
def foo(first, second=3, third):
    print(first)
    print(second)
    print(third)

foo(42)
'''
The code will result in an error because 42 will be assigned to the parameter,
'first', but the parameter, 'third', is not assigned a default value.
'''

# 14. Identify all of the identifiers on each line of the following code.
def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')
'''
multiply:       156, 164
left:           156, 157
right:          156, 157
get_num:        159, 162, 163
prompt:         159, 160
first_number:   162, 164, 165
second_number:  163, 164, 165
product:        164, 165
float:          160
input:          160
print:          165
'''

# 15. Using the code below, classify the identifiers as global, local, or
# built-in. For our purposes, you may assume this code is the entire program.
def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')
'''
Global:     multiply, get_num, first_number, second_number, product
Local:      left, right, prompt
Built-in:   float, input, print
'''

# 16. In the code shown below, identify all of the function names and
# parameters present in the code. Include the line numbers for each item
# identified.
def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')
'''
Fuction Names
multiply:   201, 209
get_num:    204, 207, 208
float:      205
input:      205
print:      210

Parameters
left:           201, 202
right:          201, 202
prompt:         204, 205
'''

# 17. Which of the identifiers in the following program are function names?
# Which are method names? Which are built-in function?
def say(message):
    print(f'==> {message}')

string1 = input()
string2 = input()

say(max(string1.upper(), string2.lower()))
'''
Function Names:
say

Method Names:
upper()
lower()

Built-in Function:
print
input
max
'''

# 18. The following function returns a list of the remainders of dividing the
# numbers in 'numbers' by 3:
def remainders_3(numbers):
    return [number % 3 for number in numbers]
# Use this function to determine which of the following list contains at least
# one number that is not evenly divisible by 3 (that is, the remainder is not
# 0):
numbers_1 = [0, 1, 2, 3, 4, 5, 6]   # True
numbers_2 = [1, 2, 4, 5]            # True
numbers_3 = [0, 3, 6]               # False
numbers_4 = []                      # False

# 19. The following function returns a list of the remainders of dividing the
# numbers in 'numbers' by 5:
def remainders_5(numbers):
    return [number % 5 for number in numbers]
# Use this function to determine which of the following lists do not contain
# any numbers that are divisible by 5:
numbers_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # False
numbers_2 = [1, 2, 3, 4, 6, 7, 8, 9]            # True
numbers_3 = [0, 5, 10]                          # False
numbers_4 = []                                  # True