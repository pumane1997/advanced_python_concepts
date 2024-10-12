
'''

Dictionaries 

This built-in data structure lets us create pairs of values where one value is associated with 
another one. We use curly brackets {} with the key-value pairs separated by a comma.

! The keys of a dictionary must be of an immutable data type. 
  For example, they can be strings, numbers, or tuples but not lists since lists are mutable.

The values of a dictionary can be of any data type

'''

my_dict = {"a": 1, "b": 2, "c": 3, "d": 4}

# Length

print(len(my_dict))

# Access a value from dict based on key

print(my_dict["a"])

# Update value in dict - we use the same syntax but now we add an assignment operator and the value

my_dict["b"] = 5
print(my_dict)

# Add key-value in dict - we use the same syntax but now we add an assignment operator and the value

my_dict["e"] = 5
print(my_dict)

# Delete key-value pair

del (my_dict["e"])
print(my_dict)


# Dictonary methods

print('----- Dictonary methods -----')

my_dict = {"a": 1, "b": 2, "c": 3, "d": 4}

print(my_dict.get("c")) # returns value based on key specified

print(my_dict.items()) # returns key-val tuples in list

print(my_dict.keys()) # returns list of keys

print(my_dict.pop("d"))

print(my_dict.popitem())

print(my_dict.setdefault("a", 15))

print(my_dict)

print(my_dict.setdefault("f", 25))

print(my_dict)

print(my_dict.update({"c": 3, "d": 4, "e": 5}))

print(my_dict.values())

print(my_dict.clear())

print(my_dict)


# Merging dictionaries

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict1.update(dict2)
print(dict1)  

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged = dict1 | dict2
print(merged)


# Iterating over dict

print('--Iterating--')
for key in dict2:
    print(key)

for value in dict2.values():
    print(value)

for key, value in dict2.items():
    print(f"{key}: {value}")

# Sorting dict

print('Sorted')

sorted_by_keys = dict(sorted(dict2.items()))
print(sorted_by_keys)

sorted_by_values = dict(sorted(dict2.items(), key=lambda item: item[1]))
print(sorted_by_values)

# Using defaultdict for default values

'''
The defaultdict from the collections module is useful when you want to avoid key errors when 
accessing or updating a dictionary
'''

from collections import defaultdict

dd = defaultdict(int)  # The default value will be 0 for non-existent keys
dd['a'] += 1
print(dd)  