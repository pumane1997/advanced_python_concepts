'''

Tuples

To define a tuple in Python, we use parentheses () and separate the elements with a comma.

Indexing & slicing is same as that of string or list (can use negative indices)

Can contain elements of different datatypes

Immutable - makes them perfect for storing constant data that should not be modified.

Use case: When you need a fixed collection of items, such as coordinates ((x, y)), 
          configuration values, or days of the week, tuples are preferable because they 
          prevent accidental modification.

Memory efficiency: Tuples generally consume less memory compared to lists. Since tuples are immutable, 
                   Python can optimize their storage more efficiently.

Use case: When handling large datasets where the data won't change, using tuples 
          can save memory and improve performance.

Performance:  Because tuples are immutable, they offer faster iteration and access compared to lists. 
              The immutability allows Python to make certain performance optimizations, such as caching and reduced overhead for memory management.

Use case: In scenarios where performance is critical and you need to access elements 
          quickly (like returning multiple values from a function), tuples can be faster.

          
Data Integrity: Tuples can be used when you want to ensure data integrity. 
                If you pass a tuple to a function, you can guarantee that the data won’t change 
                during processing.

Use case: When passing a collection of constant values or when working with sensitive or critical 
          data that should remain unchanged.

Tuples as Keys in Dictionaries: Since tuples are immutable and hashable, they can be used as keys 
                                in dictionaries, whereas lists cannot.

Use case: If you need to use compound keys in a dictionary, like combining multiple 
          fields (e.g., (city, country)), tuples are ideal.

Function Argument Packing: Tuples are often used for returning multiple values from functions. 
                           This is because of their simplicity and immutability. Python functions 
                           can return multiple values as a tuple without needing explicit creation.

Use case: When a function needs to return multiple values, tuples are a natural fit, as seen in the 
          following example:

            def get_coordinates():
                return (10, 20)  # Returns a tuple

Semantics: Tuples are often used to represent heterogeneous data (i.e., data of different types). 
           Lists, on the other hand, are typically used for homogeneous collections 
           (i.e., a collection of similar items).

Use case: Use a tuple to represent a structured object with different fields, like an employee 
          record (name, age, salary).

'''

# Tuple methods - There are two built-in tuple methods in Python

freecodecampmy_tuple = (4, 4, 5, 6, 6, 7, 8, 9, 10)

print(freecodecampmy_tuple.count(6))

print(freecodecampmy_tuple.index(7))

'''
Tip: tuples are immutable. They cannot be modified, so we can't add, update, or remove elements 
     from the tuple. If we need to do so, then we need to create a new copy of the tuple.
'''


# Tuple assignment

'''
In Python, we have a really cool feature called Tuple Assignment. 
With this type of assignment, we can assign values to multiple variables on the same line.
'''

a, b = 1, 2

print(a)

a, b = b, a    # This common way to swap the values