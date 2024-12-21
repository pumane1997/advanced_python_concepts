
'''
How Python interpreter executes under the hood

Python is not a software that you install on your computer. It is just a 
language. What you install on your computer is the interpreter. So when we execute
some code, it is interpreter that we are executing.

After running the code, there is a series of events that the interpreter goes through
that is divided in three phases - 

    - Parsing phase: Interpreter parses the code - it checks if the code is syntactically
                     correct
    - Compilation: Compiles the code into byte code - i.e. python code is translated
                   into byte code which more lower level code understood by operating
                   system.
    - Interpretation: Interpreter starts to interpret byte code and shows you the output,
                      however there might be a logical error in this phase.

Syntax errors during parsing phase are just called errors.
Errors during compilation are called exceptions (ex: Attribute, Name etc)

Parser reads code from top to bottom
Interpreter follows instructions

'''