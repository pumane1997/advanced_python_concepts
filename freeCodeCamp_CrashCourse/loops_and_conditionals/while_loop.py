
'''
While loop

While loops are similar to for loops in that they let us repeat a block of code. 
The difference is that while loops run while a condition is True.

In a while loop, we define the condition, not the number of iterations. 
The loop stops when the condition is False.

General syntax -

while <condition>:
    <code>

in while loops, you must update the variables that are part of the condition to make sure 
that the condition will eventually become False
'''

x = 6

while x < 15:
    print(x)
    x += 1

# We can also use break and continue with while loops

x = 6

while x < 15:
    if x % 2 == 0:
        print("Even:", x)
        break
    print(x)
    x += 1

x = 6

while x < 15:
    if x % 2 == 0:
        x += 1
        continue
    print("Odd:", x)
    x += 1


'''
We can also add an else clause to a while loop. If break is found, the else 
clause doesn't run but if the break statement is not found, the else clause runs.
'''

x = 5

while x < 15:
    if x % 2 == 0:
        print("Even number found")
        break
    print(x)
    x += 2
else:
    print("All numbers were odd")
