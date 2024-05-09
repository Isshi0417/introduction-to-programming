# 1. Classify the following potential non-constant variable names as idiomatic,
# non-idiomatic, or illegal. 
'''
index : idiomatic
CatName : non-idiomatic
lazy_dog : idiomatic
quick_Fox : non-idiomatic
1stCharacter : illegal
operand2 : idiomatic
BIG_NUMBER : non-idiomatic
pi : non-idiomatic
'''

# 2. Classify the following potential function names as idiomatic,
# non-idiomatic, or illegal.
'''
index : idiomatic
CatName : non-idiomatic
lazy_dog : idiomatic
quick_Fox : non-idiomatic
1stCharacter : illegal
operand2 : idiomatic
BIG_NUMBER : non-idiomatic
pi : non-idiomatic
'''

# 3. Classify the following potential constant names as idiomatic,
# non-idiomatic, or illegal.
'''
index : non-idiomatic
CatName : non-idiomatic
snake_case : non-idiomatic
LAZY_DOG3 : idiomatic
1ST : illegal
operand2 : non-idiomatic
BIG_NUMBER : idiomatic
pi : non-idiomatic
'''

# 4. Classify the following potential class names as idiomatic, non-idiomatic,
# or illegal.
'''
index : non-idiomatic
CatName : idiomatic
Lazy_Dog : non-idiomatic
1ST : illegal
operand2 : non-idiomatic
BigNumber3 : idiomatic
Pi : no-idiomatic
'''

# 5. Write a program named 'greeter.py' that greets 'Victor' three times. Your
# program should use a varriable and not hard code the string value 'Victor'
# in each greeting.
'''
File in /variables_files.
'''

# 6. Write a program named 'age.py' that includes someone's age and then 
# calculates and reports the future age 10, 20, 30, and 40 years from now.
'''
File in /variables_files.
'''

# 7. What happens when you run the following code? Why?
NAME = 'Victor'
print('Good Morning, ' + NAME)
print('Good Afternoon, ' + NAME)
print('Good Evening, ' + NAME)

NAME = 'Nina'
print('Good Morning, ' + NAME)
print('Good Afternoon, ' + NAME)
print('Good Evening, ' + NAME)
'''
The first block will print the greeting followed by the name 'Victor'.
The second block will print the greeting followed by the name 'Nina'.
This is because the variable is reassigned to the value 'Nina' since there are
no real constants in Python.
'''

# 8. This program uses a bit of math. Don't let that scare you away -- try it
# anyway.

# Assume you have $1,000.00 in the bank, and you've somehow managed to find a
# bank that pays you 5% (this is a wish-fulfillment fantasy) compounded
# interest every year. After one year, you will have $1,050 ($1,000 times 1.05)
# After two years, you will have $1,050 times 1.05, or $1102.50. Create a
# variable named 'balance' that contains the amount of money you will have
# after 5 years, then print the result.
balance = 1000 * (1.05)**5
print(balance)

# 9. Repeat the previous question but, this time, use augmented assignment to
# compute the final result, one year at a time.
balance = 1000
for i in range(1, 6):
    balance = 1000 * (1.05)**i
    print(balance)

# 10. Assume that 'obj' already has a value of '42' when the code below starts
# running. Which of the subsequent statements reassign the variable? WHich
# statements mutate the value of the object that 'obj' references? Which
# statements do neither? If necessary, you can read the documentation.
obj = 'ABcd'        # Reassignment
obj.upper()         # Neither
obj = obj.lower()   # Reassignment
print(len(obj))     # Neither
obj = list(obj)     # Reassignment
obj.pop()           # Mutation
obj[2] = 'X'        # Mutation
obj.sort()          # Mutation
set(obj)            # Neither
obj = tuple(obj)    # Reassignment