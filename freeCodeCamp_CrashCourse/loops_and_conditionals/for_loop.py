
'''
-- for --

for <loop_variable> in <iterable>:
    <code>

The iterable can be a -> list, tuple, dictionary, string, the sequence returned by range, 
                        a file, or any other type of iterable in Python.

This is the general syntax to write a for loop with range():

for <loop_variable> in range(<start>, <stop>, <step>):
    <code>

'''




'''
-- Break and Continue in Python --

We also have loop control statements to customize what happens when the loop runs: 
break and continue.

The break statement is used to stop the loop immediately.

'''

my_list = [1, 2, 3, 4, 5]

for elem in my_list:
    if elem % 2 == 0:
        print("Even:", elem)
        print("break")
        break
    else:
        print("Odd:", elem)


'''
The continue statement is used to skip the rest of the current iteration.

When it is found during the execution of the loop, the current iteration stops and a 
new one begins with the updated value of the loop variable.

'''

for elem in my_list:
    if elem % 2 == 0:
        print("continue")
        continue
    print("Odd:", elem)



'''
zip() is an amazing built-in function that we can use in Python to iterate over 
multiple sequences at once, getting their corresponding elements in each iteration.

We just need to pass the sequences as arguments to the zip() function and use 
this result in the loop.

'''

print('zip funcation')

my_list1 = [1, 2, 3, 4]
my_list2 = [5, 6, 7, 8]

for elem1, elem2 in zip(my_list1, my_list2):
    print(elem1, elem2)


'''
You can also keep track of a counter while the loop runs with the enum() function. 
It is commonly used to iterate over a sequence and get the corresponding index.
'''

print('enumerate')

my_list = [5, 6, 7, 8]

for i, elem in enumerate(my_list):
    print(i, elem)

# If you start the counter from 0, you can use the index and the current value in the same 
# iteration to modify the sequence:

for index, num in enumerate(my_list):
    my_list[index] = num * 3

print(my_list)

# You can start the counter from a different number by passing a second argument to enumerate():

word = "Hello"

for i, char in enumerate(word, 2):
    print(i, char)

