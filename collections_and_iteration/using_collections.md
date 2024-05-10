# Using Collections

##### *1. Write Python code to print the seventh number of `range(0, 25, 3)`.*

```python
print(range(0, 25, 3)[6])
```

##### *2. Use slicing to write Python code to print a 6-character substring of `'Launch School'` that begins with the first `c`.*

```python
print('Launch School'[slice(4, 10)])
```

##### *3. Write Python code to create a new tuple from `(1, 2, 3, 4, 5)`. The new tuple should be in reverse order from the original. It should  also exclude the first and last members of the original. The result  should be the tuple `(4, 3, 2)`.*

```python
count = (1, 2, 3, 4, 5)
count_list = list(count)
count_list.reverse()
print(tuple(count_list[1 : 4]))
```

##### *4. This is a 3-part question. Consider the following dictionary:*

```python
pets = {
    'Cat':  'Meow',
    'Dog':  'Bark',
    'Bird': 'Tweet',
}
```

##### *Part 1: Write some code to print `Bark` by accessing the element associated with the key `Dog`.*

```python
print(pets.get('Dog'))
```

##### *Part 2: Write some code to print `None` when you try to print the value associated with the non-existent key, `Lizard`*

```python
print(pets.get('Lizard'))
```

##### ***Part 3**: Write some code to print `<silence>` when you try to print the value associated with the non-existent key, `Lizard`.*

```python
print(pets.get('Lizard', '<silence>'))
```

##### *5. Which of the following values **can't** be used as a key in a `dict` object, and why?*

```python
'cat'
(3, 1, 4, 1, 5, 9, 2)
['a', 'b']
{'a': 1, 'b': 2}
range(5)
{1, 4, 9, 16, 25}
3
0.0
frozenset({1, 4, 9, 16, 25})
```

`['a', 'b']`, `{'a' : 1, 'b' : 2}`, `{1, 4, 9, 16, 25}` because they are all mutable.

##### *6. What will the following code print?*

```python
print('abc-def'.isalpha())		# False
print('abc_def'.isalpha())		# False
print('abc def'.isalpha())		# False
print('abc def'.isalpha() and
      'abc def'.isspace())		# False
print('abc def'.isalpha() or
      'abc def'.isspace())		# False
print('abcdef'.isalpha())		# True
print('31415'.isdigit())		# True
print('-31415'.isdigit())		# False
print('31_415'.isdigit())		# False
print('3.1415'.isdigit())		# False
print(''.isspace())				# False
```

##### *7. Write Python code to replace all the `:` characters in the string below with `+`.*

```python
info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'

print('+'.join(info.split(':')))
```

##### *Try this problem using the methods you've learned about in this chapter. Once you have that working, use the Python documentation for the `str` type to find an alternative solution.*

```python
print(info.replace(':', '+'))
```

##### *8. Explain why the code below prints different values on lines 3 and 4.*

```python
text = "It's probably pining for the fjords!"

print(text[21:35].rfind('f'))     # 8
print(text.rfind('f', 21, 35))    # 29
```

Line 3 gets a slice from `text` between the index 21 and 35 and returns the string from the sliced text: `for the fjords!`. In this case, when searched from the right hand side, the first `f` is located at index 8.

Line 4 starts searching from the right hand side between the index 21 and 35 of the original `text`, and the first `f` is located at index 29.

##### *9. Write some code to replace the value `6` in the following nested list with `606`. You don't have to search the list. Just write an assignment that replaces the `6`.*

```python
stuff = [
    ['hello', 'world'],
    ['example', 'mem', None, 6, 88],
    [4, 8, 12],
]

stuff[1][3] = 606
```

##### *10. Consider the following nested collection. Write one line of code to print the activities that Cocoa enjoys.*

```python
cats = {
    'Pete': {
        'Cheddar': {
            'color': 'orange',
            'enjoys': {
                'sleeping',
                'snuggling',
                'meowing',
                'eating',
                'birdwatching',
            },
        },
        'Cocoa': {
            'color': 'black',
            'enjoys': {
                'eating',
                'sleeping',
                'playing',
                'chewing',
            },
        },
    },
}

print(cats['Pete']['Cocoa']['enjoys'])
```

##### *11. Without running the following code, determine what each line should print.*

```python
print('johnson' in 'Joe Johnson')		# False
print('sen' not in 'Joe Johnson')		# True
print('Joe J' in 'Joe Johnson')			# True
print(5 in range(5))					# False
print(5 in range(6))					# True
print(5 not in range(5, 10))			# False
print(0 in range(10, 0, -1))			# False
print(4 in {6, 5, 4, 3, 2, 1})			# True
print({1, 2, 3} in {1, 2, 3})			# False
print({3, 2} in {1, frozenset({2, 3})})	# True
```

##### *12. Write some code that determines and prints whether the number `3` appears inside each of these lists. You should print `True` or `False` depending on each result.*

```python
numbers1 = [1, 3, 5, 7, 9, 11]
numbers2 = []
numbers3 = [2, 4, 6, 8]
numbers4 = ['1', '3', '5']
numbers5 = ['1', 3.0, '5']

print(3 in numbers1)	# True
print(3 in numbers2)	# False
print(3 in numbers3)	# False
print(3 in numbers4)	# False
print(3 in numbers5)	# True
```

##### *13. Without running the following code, determine what each print statement should print.*

```python
cats = ('Cocoa', 'Cheddar',
        'Pudding', 'Butterscotch')
print('Butterscotch' in cats)		# True
print('Butter' in cats)				# False
print('Butter' in cats[3])			# True
print('cheddar' in cats)			# False
```

##### *14. Assume you have the following sequences. Write some code that combines the sequences into a list of tuples. Each  tuple should contain one member of each sequence.*

```python
my_str = 'abc'
my_list = ['Alpha', 'Bravo', 'Charlie']
my_tuple = (None, True, False)
my_range = range(10, 60, 10)

print(tuple(zip(my_str, my_list, my_tuple, my_range)))
```

##### *15. Without running the following code, what values will be printed by line 10?*

```python
pets = {
    'Cat':  'Meow',
    'Dog':  'Bark',
    'Bird': 'Tweet',
}

keys = pets.keys()
del pets['Dog']
pets['Snake'] = 'Sssss'
print(keys)				# dict_keys(['Cat', 'Bird', 'Snake'])
```

