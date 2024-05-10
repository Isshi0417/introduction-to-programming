# Input/Output

##### *1. Write a program named `greeter.py`. The program should ask for your name, then output `Hello, NAME!` where `NAME` is the name you entered:*

```python
name = input('What is your name?\n')
print(f'Hello, {name}!')
```

File in `/inputs_and_outputs_files/greeter.py`

##### *2. Modify the `greeter.py` program to ask for the user's first and last names separately, then greet the user with their full name.*

```python
first_name = input('What is your first name? ')
last_name = input('What is your last name? ')
print(f'Hello, {first_name} {last_name}!')
```

File in `/inputs_and_outputs_files/greeter.py`.

##### *3. Write a program named `age.py` that asks the user to enter  their age, then calculates and reports the future age 10, 20, 30, and 40 years from now. Here's the output for someone who is 27 years old.*

```python
age = int(input('How old are you? '))
print(f'In 10 years, you will be {age + 10} years old')
print(f'In 20 years, you will be {age + 20} years old')
print(f'In 30 years, you will be {age + 30} years old')
print(f'In 40 years, you will be {age + 40} years old')
```

File in `/inputs_and_outputs_files/age.py`.