
'''
Exception handling

An error or unexpected event that that occurs while a program is running is called an exception. 
We can avoid terminating the program abruptly when this occurs.

Common Exceptions in Python:
- ZeroDivisionError: raised when the second argument of a division or modulo operation is zero.
- IndexError: raised when we try to use an invalid index to access an element of a sequence.
- KeyError: raised when we try to access a key-value pair that doesn't exist because the 
  key is not in the dictionary.
- NameError: raised when we use a variable that has not been defined previously.
- RecursionError: raised when the interpreter detects that the maximum recursion depth is 
  exceeded.
'''


'''
try / except in Python
We can use try/except in Python to catch the exceptions when they occur and handle 
them appropriately. This way, the program can terminate appropriately or even recover 
from the exception.

This is the basic syntax:

try:
    <code_that_may_raise_an_exception>
except:
    <code_to_handle_the_exception_if_it_occurs>
'''


'''
How to Catch a Specific Type of Exception in Python
Instead of catching and handling all possible exceptions that could occur in the try clause, 
we could catch and handle a specific type of exception. We just need to specify the type of 
the exception after the except keyword:

try:
    <code_that_may_raise_an_exception>
except <exception_type>:
    <code_to_handle_an_exception_if_it_occurs>
'''

print('example 1')

index = int(input("Enter the index: "))

try:
    my_list = [1, 2, 3, 4]
    print(my_list[index])
except IndexError: # specify the type
    print("Please enter a valid index.")

print('example 2')

a = int(input("Enter a: "))
b = int(input("Enter b: "))

try:
    division = a / b
    print(division)
except ZeroDivisionError: # specify the type
    print("Please enter valid values.")


'''
How to Assign a Name to the Exception Object in Python
We can specify a name for the exception object by assigning it to a variable that we can 
use in the except clause. This will let us access its description and attributes.

We only need to add as <name>, like this:

try:
    <code_that_may_raise_an_exception>
except <exception_type> as <name>:
    <code_to_handle_an_exception_if_it_occurs>

'''

print('example 31')

index = int(input("Enter the index: "))

try:
    my_list = [1, 2, 3, 4]
    print(my_list[index])
except IndexError as e:
    print("Exception raised:", e)


'''
try / except / else in Python

We can add an else clause to this structure after except if we want to choose what happens 
when no exceptions occur during the execution of the try clause:

try:
    <code_that_may_raise_an_exception>
except:
    <code_to_handle_an_exception_if_it_occurs>
else:
    <code_that_only_runs_if_no_exception_in_try>

'''

print('example 4')

a = int(input("Enter a: "))
b = int(input("Enter b: "))

try:
    division = a / b
    print(division)
except ZeroDivisionError as err:
    print("Please enter valid values.", err)
else:
    print("Both values were valid.")


'''
try / except / else / finally in Python
We can also add a finally clause if we need to run code that should always run, 
even if an exception is raised in try.
'''

print('example 5')

a = int(input("Enter a: "))
b = int(input("Enter b: "))

try:
    division = a / b
    print(division)
except ZeroDivisionError as err:
    print("Please enter valid values.", err)
else:
    print("Both values were valid.")
finally:
    print("Finally!")

# 💡 Tip: this clause can be used, for example, to close files even if the code throws 
# an exception.