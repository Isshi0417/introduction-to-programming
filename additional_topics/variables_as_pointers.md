# Variables as Pointers

##### *1. In your own words, explain the difference between these two expressions.*

```python
my_object1 == my_object2
my_object1 is my_object2
```

Line 1 compares the values of the two objects, whereas line 2 compares whether the object itself (or the referenced object) is equivalent. 

##### *2. Without running this code, what will it print? Why?*

```python
set1 = {42, 'Monty Python', ('a', 'b', 'c')}
set2 = set1
set1.add(range(5, 10))
print(set2)	# {42, 'Monty Python', ('a', 'b', 'c'), range(6, 10)}
```

This is because `set2` is assigned as `set1`, which means the referenced object is the same. Since adding an element to `set1` mutates it, it also mutates `set2`.

##### *3. Without running this code, what will it print? Why?*

```python
dict1 = {
    "Hitchhiker's Guide to the Galaxy": 42,
    'Monty Python': 'The Life of Brian',
    'Airplane!': "Don't call me Shirley!",
}

dict2 = dict(dict1)
dict2['Monty Python'] = 'Holy Grail'
print(dict1['Monty Python'])	# 'The Life of Brian'
```

This is because `dict2` and `dict1` do not reference the same object. `dict2 = dict(dict1)` creates a new dictionary, which means the change is not reflected in `dict2`. (However, any changes in `dict1` will be reflected in `dict2`)

##### *4. Without running this code, what will it print? Why?*

```python
dict1 = {
    'a': [1, 2, 3],
    'b': (4, 5, 6),
}

dict2 = dict(dict1)
dict1['a'][1] = 42
print(dict2['a'])	# [1, 42, 3]
```

This is because `dict2` shares the same value components as `dict1`. While they don't reference the same objects, any changes made in `dict1` still affects `dict2` as a shallow copy.

##### *5. Write some code to create a deep copy of the `dict1` object and assign it to `dict2`. You should only modify the code where indicated.*

```python
import copy	# modified line

dict1 = {
    'a': [[7, 1], ['aa', 'aaa']],
    'b': ([3, 2], ['bb', 'bbb']),
}

dict2 = copy.deepcopy(dict1)	# modified line

# All of these should print False
print(dict1         is dict2)
print(dict1['a']    is dict2['a'])
print(dict1['a'][0] is dict2['a'][0])
print(dict1['a'][1] is dict2['a'][1])
print(dict1['b']    is dict2['b'])
print(dict1['b'][0] is dict2['b'][0])
print(dict1['b'][1] is dict2['b'][1])
```

##### *6. The following program is nearly identical to that of the previous  exercise. However, this time, it should create a shallow copy of `dict1`. Be careful: **you're not allowed to use the `copy` module in this exercise**. In addition, before you run this code, can you predict the output values?*

```python
dict1 = {
    'a': [{7, 1}, ['aa', 'aaa']],
    'b': ({3, 2}, ['bb', 'bbb']),
}

dict2 = dict(dict1)    # modified line

print(dict1         is dict2)		# False
print(dict1['a']    is dict2['a'])	# True
print(dict1['a'][0] is dict2['a'][0])	# True
print(dict1['a'][1] is dict2['a'][1])	# True
print(dict1['b']    is dict2['b'])	# True
print(dict1['b'][0] is dict2['b'][0])	# True
print(dict1['b'][1] is dict2['b'][1])	# True
```

