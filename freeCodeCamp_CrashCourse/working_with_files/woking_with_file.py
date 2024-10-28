
'''
Working with files

In Python, it's recommended to use a with statement to work with files because it opens 
them only while we need them and it closes them automatically when the process is completed.

To read a file, we use this syntax:

with open("<file_path>") as <file_var>:
    <code>

We can also specify that we want to open the file in read mode with an "r":

with open("<file_path>", "r") as <file_var>:
    <code>

    
But this is already the default mode to open a file, so we can omit it like in the 
first example.

'''

file_dir = 'C:\\dev\\advanced_python_concepts\\freeCodeCamp_CrashCourse\\working_with_files\\'

with open(file_dir+'\\example.txt', 'r') as ex_file:
    for line in ex_file:
        print(line)


'''
Writing file

There are two ways to write to a file - completely overwrite or append

We use 'w' arg in open function and call .write method in the code to write string
'''

# Overwrite

words = ['Raahithya', 'Champion']

with open(file_dir+'example_2.txt', 'w') as ex_file:
    for word in words:
        ex_file.write(word + '\n')
    print('done')

# Append

words = ['winner']

with open(file_dir+'example_2.txt', 'a') as ex_file:
    for word in words:
        ex_file.write(word + '\n')
    print('done')

# Dalete

'''
To delete a file with our script, we can use the os module. It is recommended to check 
with a conditional if the file exists before calling the remove() function from this module:
'''

import os
if os.path.exists(file_dir+'example_3.txt'):
    os.remove(file_dir+'example_3.txt')
else:
    pass

