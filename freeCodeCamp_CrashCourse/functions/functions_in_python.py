'''
In Python, we can define functions to make our code reusable, more readable, and organized. 

This is the basic syntax of a Python function:

def <function_name>(<param1>, <param2>, ...):
    <code>

- A function can have zero, one, or multiple parameters

If you want your function to return something on calling it, use 'return'
If you just want it to do something, define in that code

The function stops immediately when return is found and the value is returned.

We can also use return with a conditional to return a value based on whether a 
condition is True or False.

If a function doesn't have a return statement or doesn't find one during its execution, 
it returns None by default

The Style Guide for Python Code recommends using return statements consistently. 

It mentions that we should:

Be consistent in return statements. Either all return statements in a function should return 
an expression, or none of them should. If any return statement returns an expression, 
any return statements where no value is returned should explicitly state this as return None, 
and an explicit return statement should be present at the end of the function (if reachable)

Default Arguments in Python
We can assign default arguments for the parameters of our function. 
To do this, we just need to write <parameter>=<value> in the list of parameters.

💡 Tip: The Style Guide for Python Code mentions that we shouldn't "use spaces around 
        the = sign when used to indicate a keyword argument."

Parameters with default arguments have to be defined at the end of the list of parameters. 
Else, you will see this error: SyntaxError: non-default argument follows default argument

'''

