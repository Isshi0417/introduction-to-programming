# Functions and Methods

###### *1. What happens when you run the following program? Why do we get that result?*

```python
def set_foo():
    foo = 'bar'

set_foo()
print(foo)
```

`set_foo()` successfully assigns the value `bar` to the variable `foo`. However, printing `foo` will result in an error because `foo` is a local variable that only exists while the function is called.

###### *2. Take a look at this code snippet. What does this program print and why?*

```python
foo = 'bar'

def set_foo():
    foo = 'qux'

set_foo()
print(foo)
```

The program will print `bar`. This is because the function creates a local variable and assigns the value to the newly created variable, which means that the value of `foo` outside the function is not changed.

###### *3. Write a program that uses a `multiply` function to multiply  two numbers and returns the result. Ask the user to enter the two  numbers, then output the numbers and result as a simple equation.*

```python
def multiply():
    a = input('Enter the first number: ')
    b = input('Enter the second number: ')
    print(f'{a} * {b} = {float(a) * float(b)}')
```

###### *4. Consider this code. Identify the following items in that code.*

```python
def multiply_numbers(num1, num2, num3):
    result = num1 * num2 * num3
    return result

product = multiply_numbers(2, 3, 4)
```

| Item                  | **Identification**                                           |
| :-------------------- | ------------------------------------------------------------ |
| function name         | `multiply_numbers` (1, 5)                                    |
| function arguments    | `2`, `3`, `4` (5)                                            |
| function definition   | `def multiply_numbers(num1, num2, num3):` (1)                |
| function body         | `result = num1 * num2 * num3`<br />`return result` (2, 3)    |
| function parameters   | `num1`, `num2`, `num3` (1)                                   |
| function invocation   | `multiply_numbers(2, 3, 4)` (5)                              |
| function return value | `return result` (3)                                          |
| all identifiers       | `multiply_numbers`, `num1`, `num2`, `num3`, `result`, `product` |

###### *5. What does the following code print?*

```python
def scream(words):
    return words + '!!!!'

scream('Yipeee')
```

The code prints nothing because the function returns the value instead of printing it.

###### *6. What does the following code print?*

```python
def scream(words):
    words = words + '!!!!'
    return
    print(words)

scream('Yipeee')
```

The code prints nothing because the function terminates itself after `return`.

###### *7. Without running the following code, what do you think it will do?*

```python
def foo(bar, qux):
    print(bar)
    print(qux)

foo('Hello')
```

The code will result in an error because function `foo` is defined with two parameters, but the function is called with only one argument.

###### *8. Without running the following code, what do you think it will do?*

```python
def foo(bar, qux):
    print(bar)
    print(qux)

foo(42, 3.141592, 2.718)
```

The code will result in an error because function `foo` is defined with two parameters, but the function is called with three arguments.

###### *9. Without running the following code, what do you think it will do?*

```python
def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42, 3.141592, 2.718)
```

The code will print `42`, `3.141592`, and `2.718` respectively in their own lines.

###### *10. Without running the following code, what do you think it will do?*

```python
def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42, 3.141592)
```

he code will print `42`, `3.141592`, and `2` respectively in their own lines.

###### *11. Without running the following code, what do you think it will do?*

```python
def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42)
```

The code will print `42`, `3`, and `2` respectively in their own lines.

###### *12. Without running the following code, what do you think it will do?*

```python
def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo()
```

The code will result in an error because the parameter, `first`, is not assigned a default value.

###### *13. Without running the following code, what do you think it will do?*

```python
def foo(first, second=3, third):
    print(first)
    print(second)
    print(third)

foo(42)
```

The code will result in an error because 42 will be assigned to the parameter, `first`, but the parameter, `third`, is not assigned a default value.

###### *14. Identify all of the identifiers on each line of the following code.*

```python
def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')
```

| **Identifier** | **Line Number** |
| -------------- | --------------- |
| multiply       | 1, 9            |
| left           | 1, 2            |
| right          | 1, 2            |
| right_num      | 7, 9, 10        |
| prompt         | 8, 9, 10        |
| first_number   | 4, 7, 8         |
| second_number  | 4, 5            |
| product        | 5               |
| float          | 5               |
| input          | 9, 10           |
| print          | 10              |

###### *15. Using the code below, classify the identifiers as global, local, or  built-in. For our purposes, you may assume this code is the entire  program.*

```python
def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')
```

| **Category** | **Identifier**                                               |
| ------------ | ------------------------------------------------------------ |
| Global       | `multiply`, `get_num`, `first_number`, `second_number`, `product` |
| Local        | `left`, `right`, `prompt`                                    |
| Built-in     | `float`, `input`, `print                                     |

###### *16. In the code shown below, identify all of the function names and  parameters present in the code. Include the line numbers for each item identified.*

```python
def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')
```

| **Function Names** |
| ------------------ |
| `multiply`: 1, 9   |
| `get_num`: 4, 7    |
| `float`: 5         |
| `input`: 5         |
| `print`: 10        |

| **Parameters**        |
| --------------------- |
| `left`, `right`: 1, 2 |
| `prompt`: 4, 5        |

###### *17. Which of the identifiers in the following program are function names? Which are method names? Which are built-in functions?*

```python
def say(message):
    print(f'==> {message}')

string1 = input()
string2 = input()

say(max(string1.upper(), string2.lower()))
```

| **Function Names** |
| ------------------ |
| `say`              |

| **Method Names** |
| ---------------- |
| `upper`          |
| `lower`          |

| **Built-in Function Names** |
| --------------------------- |
| `print`                     |
| `input`                     |
| `max`                       |

###### *18. The following function returns a list of the remainders of dividing the numbers in `numbers` by 3. Use this function to determine which of the following lists contains at least one number that is **not** evenly divisible by 3 (that is, the remainder is not `0`):*

```python
def remainders_3(numbers):
    return [number % 3 for number in numbers]

numbers_1 = [0, 1, 2, 3, 4, 5, 6]   # True
numbers_2 = [1, 2, 4, 5]            # True
numbers_3 = [0, 3, 6]               # False
numbers_4 = []                      # False
```

###### *19. The following function returns a list of the remainders of dividing the numbers in `numbers` by 5. Use this function to determine which of the following lists do not contain any numbers that are divisible by 5:*

```python
def remainders_5(numbers):
    return [number % 5 for number in numbers]

numbers_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # False
numbers_2 = [1, 2, 3, 4, 6, 7, 8, 9]            # True
numbers_3 = [0, 5, 10]                          # False
numbers_4 = []                                  # True
```

