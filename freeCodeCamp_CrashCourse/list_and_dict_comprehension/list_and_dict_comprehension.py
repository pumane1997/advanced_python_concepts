'''
This is just a way to create lists and dictionaries more compactly

List Comprehension

different patterns -

[<value_to_include> for <var> in <sequence>]

[<value_to_include> for <var1> in <sequence1> for <var2> in <sequence2>]

[<value_to_include> for <var> in <sequence> if <condition>]

[<value> for <var1> in <sequence1> for <var2> in <sequence2> if <condition>]

'''

print('1 - ', [i for i in range(4, 15)])

print('2 - ', [chr(i) for i in range(67, 80)])

print('3 - ', [i + j for i in range(5, 8) for j in range(3, 6)]) # if the range are not of same len then how will it work?

print('4 - ', [k for k in range(3, 35) if k % 2 == 0])

print('5 - ', [i * j for i in range(2, 6) for j in range(3, 7) if i % j == 0])


'''
List Comprehensions vs. Generator Expressions in Python

List comprehensions are defined with square brackets []. This is different from generator 
expressions, which are defined with parentheses (). They look similar but they are quite 
different. Let's see why.

List comprehensions generate the entire sequence at once and store it in memory.

Generator expressions yield the elements one at a time when they are requested.

We can use generator expressions to iterate in a for loop and get the elements one at a 
time. But if we need to store the elements in a list, then we should use list comprehension.

We can check this with the sys module. In the example below, you can see that their size in 
memory is very different:

'''

import sys
print(sys.getsizeof([i for i in range(500)]))
print(sys.getsizeof((i for i in range(500))))


'''
Dict Comprehension

The basic syntax that we need to use to define a dictionary comprehension is:

{<key_value>: <value> for <var> in <sequence>}
{<key_value>: <value> for <var> in <sequence> if <condition>}

'''

print({num: num**3 for num in range(3, 15)})

print({x: x + y for x in range(4, 8) for y in range(3, 7)})

grades = {"Nora": 78, "Gino": 100, "Talina": 56, "Elizabeth": 45, "Lulu": 67}

approved_students = {student: grade for (student, grade) in grades.items() if grade >= 60}

print(approved_students)