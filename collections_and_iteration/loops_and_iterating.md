# Loops and Iterating

##### *1. The following code causes an infinite loop (a loop that never stops iterating). Why?*

```python
counter = 0

while counter < 5:
    print(counter)
```

The code will cause an infinite loop because the counter will always be less than 5.

##### *2. Modify the `age.py` program you wrote in Exercise 3 of the [Input/Output chapter](https://launchschool.com/books/python/read/input_output#exercises). The updated code should use a `for` loop to display the future ages.*

```python
age = int(input('How old are you? '))

for i in range(10, 50, 10):
    print(f'In {i} years, you will be {age + i} years old.')
```

##### *3. Use a `while` loop to print the numbers in `my_list`, one number per line. Then, do the same with a `for` loop.*

```python
my_list = [6, 3, 0, 11, 20, 4, 17]

# while loop
count = 0
while count < len(my_list):
    print(my_list[count])
    count += 1

# for loop
for i in range(len(my_list)):
    print(my_list[i])
```

##### *4. Use a `while` loop to print all numbers in `my_list` with **even** values, one number per line. Then, print the **odd** numbers using a ' for' loop.*

```python
my_list = [6, 3, 0, 11, 20, 4, 17]

# while loop
count = 0
while count < len(my_list):
    if my_list[count] % 2 == 0:
        print(my_list[count])
    count += 1

# for loop
for i in range(len(my_list)):
    if my_list[i] % 2 != 0:
        print(my_list[i])
```

##### *5. Print all of the even numbers in the following list of nested lists. Don't use any `while` loops.*

```python
my_list = [
    [1, 3, 6, 11],
    [4, 2, 4],
    [9, 17, 16, 0],
]

for list in my_list:
    for element in list:
        if element % 2 == 0:
            print(element)
```

##### *6. We'll return to the simpler one-dimensional version of `my_list`. In this problem, you should write code that creates a new list with one element for each number in `my_list`. If the original number is an even, then the corresponding element in the new list should contain the string `'even'`; otherwise, the element should contain `'odd'`.*

```python
my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]

output = []
for element in my_list:
    if element % 2 != 0:
        output.append('odd')
    else:
        output.append('even')

print(output)
```

##### *7. Write a `find_integers` function that returns a list of all the integers from  `my_tuple`:*

```python
my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)
integers = find_integers(my_tuple)
print(integers)                    # [1, 3, -4]

output = []
def find_integers(any_tuple):
    for element in any_tuple:
        if type(element) is int:
            output.append(element)
    return output

integers = find_integers(my_tuple)
print(integers)                    # [1, 3, -4]
```

##### *8. Write a comprehension that creates a `dict` object whose keys are strings and whose values are the length of the corresponding key.  Only keys with odd lengths should be in the dict. Use the set given by `my_set` as the source of strings.*

```python
my_set = {
    'Fluffy',
    'Butterscotch',
    'Pudding',
    'Cheddar',
    'Cocoa',
}

my_dict = {}
for element in my_set:
    if len(element) % 2 != 0:
        my_dict[element] = len(element)
    
print(my_dict)
```

##### *9. Write a function that computes and returns the factorial of a number by using a `for` or `while` loop. The factorial of a positive integer `n`, signified by `n!`, is defined as the product of all integers between `1` and `n`, inclusive. You may assume that the argument is always a positive integer.*

|  n!  | Expansion           | Result |
| :--: | :------------------ | :----: |
| `1!` | `1`                 |   1    |
| `2!` | `1 * 2`             |   2    |
| `3!` | `1 * 2 * 3`         |   6    |
| `4!` | `1 * 2 * 3 * 4`     |   24   |
| `5!` | `1 * 2 * 3 * 4 * 5` |  120   |

```python
def factorial(n):
    product = 1
    while n > 0:
        product *= n
        n -= 1
    print(product)

factorial(5)
```

##### *10. The following code uses the `randrange` function from Python's `random` library to obtain and print a random integer within a given range. Using a `while` loop, it keeps running until it finds a random number that matches the  last number in the range. Refactor the code so it doesn't require two  different invocations of `randrange`.*

```python
import random

highest = 10
number = random.randrange(highest + 1)
print(number)

while number != highest:
    number = random.randrange(highest + 1)
    print(number)
    
# modified code
import random

highest = 10
while True:
    number = random.randrange(highest + 1)
    print(number)
    if number == highest:
        break
```

##### *11. Print all of the even numbers in the following list of nested lists. This time, don't use any `for` loops.*

```python
my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]

first_index = 0
while first_index < len(my_list):
    second_index = 0
    while second_index < len(my_list[first_index]):
        number = my_list[first_index][second_index]
       	if (number % 2 == 0):
            print(number)
            second_index += 1
    	second_index += 1
    first_index += 1
```

