# Intro to Collections

##### *1. If you have a list named `people`, how can you determine the number of entries in that list?*

`len(people)` can be used to determine the number of entries in the list.

##### *2. Can you write some code to change the value `'bye'` in the following tuple to `'goodbye'`?*

```python
stuff = ('hello', 'world', 'bye', 'now')

stuff_list = list(stuff)    # change to list
stuff_list[2] = 'goodbye'
stuff = tuple(stuff_list)   # change back to tuple
print(stuff)
```

##### *3. Identify at least 2 differences between lists and tuples. Identify at least 2 ways that lists and tuples are similar.*

| **Differences**                                              | **Similarities**        |
| ------------------------------------------------------------ | ----------------------- |
| Lists are mutable while tuples are not.                      | Both are sequences.     |
| List are expressed as `[]` while tuples are expressed as `()`. | Both are heterogeneous. |

##### *4. Why can we treat strings as sequences?*

Strings can be treated as sequences because they are just an ordered 'list' of characters that can be accessed with indexes.

##### *5. How do the set types differ from the sequence types?*

Unlike sequence types, set types are unordered and do not support indexes.

##### *6. Assuming you have the following assignment, write some code that converts the value of `pi` to a string and assigns it to a variable named `str_pi`.*

```python
pi = 3.141592

str_pi = str(pi)
```

##### *7. Without running the following code, identify the numbers that are included in each of the following ranges:*

```python
range(7)			# 0, 1, 2, 3, 4, 5, 6
range(1, 6)			# 1, 2, 3, 4, 5
range(3, 15, 4)		# 3, 7, 11
range(3, 8, -1)		# No numbers
range(8, 3, -1)		# 8, 7, 6, 5, 4
```

##### *8. How would you print all the numbers in the following range?*

```python
range(3, 17, 4)

print(tuple(range(3, 17, 4)))
```

##### *9. Given the above code, answer the following questions and explain your answers:*

```python
my_list = [1, 2, 3, [4, 5, 6]]
another_list = list(my_list)
```

##### *a. Are the lists assigned to `my_list` and `another_list` equal*?

Yes, they are equal that share the same elements.

##### *b. Are the lists assigned to `my_list` and `another_list` the same object?*

No, they are not the same objects because `list()` creates a new object.

##### *c. Are the nested lists at index 3 of `my_list` and `another_list` equal?* 

Yes, because they share the same elements.

##### *d. Are the nested lists at index 3 of `my_list` and `another_list` the same object?*

Yes because `list()` creates a copy of that references the nested list instead of creating a new one.

##### *10. Bob expects the following code to print the names in alphabetical order. Without running the code, can you say whether it will? Explain your  answer.*

```python
names = { 'Chris', 'Clare', 'Karis', 'Karl',
          'Max', 'Nick', 'Victor' }
print(names)
```

No, because sets are unordered collections. This means that the order of the items printed will not necessarily be in alphabetical order.

##### *11. Consider the data in the following table. You need to write some Python code to determine the country name  associated with one of the listed names. Your code should include the  data structure(s) you need and at least one test case to ensure the code works.*

| Name      | Country |
| :-------- | :------ |
| Alice     | USA     |
| Francois  | Canada  |
| Inti      | Peru    |
| Monika    | Germany |
| Sanyu     | Uganda  |
| Yoshitaka | Japan   |

```python
ethnic_names = {
    'Alice'	: 		'USA',
    'Francois' :	'Canada',
    'Inti' :		'Peru',
    'Monika' :		'Germany',
    'Sanyu' :		'Uganda',
    'Yoshitaka' :	'Japan',
}

print(ethnic_names['Yoshitaka'])
```

