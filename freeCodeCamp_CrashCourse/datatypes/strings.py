
'''
Strings - immutable dtype

They contain a sequence of characters and they are usually used to represent 
text in the code.

Quotes Within Strings
If we define a string with double quotes "", then we can use single quotes within 
the string. For example:
"I'm 20 years old"
'''



'''
String Indexing
We can use indices to access the characters of a string in our Python program. An index is an integer that represents a specific position in the string. They are associated to the character at that position.

This is a diagram of the string "Hello":

String:  H e l l o
Index:   0 1 2 3 4

'''

my_string = 'pratik'

print(my_string[1])

# we can also use negative indexing

print(my_string[-1]) #gives the last value

# String slicing -> <string_variable>[start:stop:step]

print(my_string[1:5:2])

'''
Tip: Notice that if the value of a parameter goes beyond the valid range of indices, 
    the slice will still be presented. This is how the creators of Python implemented 
    this feature of string slicing.

    And we can omit a parameter to use its default value. We just have to include the 
    corresponding colon (:) if we omit start, stop, or both:

'''

print(my_string[1:10])

print(my_string[::-1]) #step can be negative & this is easy way to reverse string


#-----


# f-strings -> parameterize the string output

first_name = "Pratik"
favorite_language = "Python"

print(f"Hi, I'm {first_name}. I'm learning {favorite_language}.")

# we can also have expression as parameter

value = 5

print(f"{value} multiplied by 2 is: {value * 2}")

# we can also call methods within the curly braces

freecodecamp = "FREECODECAMP"

print(f"{freecodecamp.lower()}")


'''
String Methods

Strings have methods, which represent common functionality that has been implemented by Python developers, so we can use it in our programs directly. They are very helpful to perform common operations.

This is the general syntax to call a string method:

<string_variable>.<method_name>(<arguments>)

'''


freecodecamp = "freeCodeCamp"

print('----- String Methods -----')

print(freecodecamp.capitalize())

print(freecodecamp.count("C"))

print(freecodecamp.find("e")) # this is returning the index of first found 

print(freecodecamp.index("p"))

print(freecodecamp.isalnum())

print(freecodecamp.isalpha())

print(freecodecamp.isdecimal())

print(freecodecamp.isdigit())

print(freecodecamp.isidentifier())

print(freecodecamp.islower())

print(freecodecamp.isnumeric())

print(freecodecamp.isprintable())

print(freecodecamp.isspace())

print(freecodecamp.istitle())

print(freecodecamp.isupper())

print(freecodecamp.lower())

print(freecodecamp.lstrip("f"))

print(freecodecamp.rstrip("p"))

print(freecodecamp.replace("e", "a"))

print(freecodecamp.split("C"))

print(freecodecamp.swapcase())

print(freecodecamp.title())

print(freecodecamp.upper())