# 1. Concatenate two strings, one with your first name and one with your last,
# to create a new string with your full name as its value.
full_name = 'Sho ' + 'Ishida'

# 2. This question may be a little challenging if your math skills are rusty.
# Don't be afraid to take advantage of the hints. Try your best to solve the
# problem, but don't feel compelled to complete it if you become frustrated.
number = 4936
ones = number % 10

number // 10
tens = number % 10

number // 10
hundreds = number % 10

thousands = number // 10

# 3. What does the following code do? Why?
print('5' + '10')
'''
The code concatenates the two values because they are both strings. 
It would output the value: 510
'''

# 4. Refractor the code form the previous exercise to use coercion to print 15
# instead.
print(int('5') + int('10'))

# 5. Will an error occur if you try to access a list element with an index
# greater than or equal to the list's length?
'''
Yes, there would be an error because the length of the list is the number of
items in the list minus one. This is because the first index is 0.
'''

# 6. To what value does the following expression evalute?
'foo' == 'FOO'
'''
The code will evaluate if whether the characters are equal to one another.
Python is able to compare lowercase and uppercase letters, which means the
expression will result in 'False'
'''

# 7. What will the following code do? Why?
int('3.1415')
'''
The will coerce the string into an integer. This means that the type of the
value inside the int() operation will change to an integer.
'''

# 8. To what value does the following expression evaluate?
'12' < '9'
'''
Python does a character-by-character comparison since they are string values.
The result will be 'True' because the the first comparison judges that
'1' < '9'.
'''