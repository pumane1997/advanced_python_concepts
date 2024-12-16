
'''
When we import another python file (like we do with module) in our main.py file, 
it imports as well as executes the whole file. So the classes and the functions
would be imported and any other code apart from it will be executed. To avoid 
excecuting any testing code, we use -

if __name__ == '__main__':

and put all the execution part inside this.

The meaning of that part is - execute this part only if this script is directly being
executed, and not through any other script.

If you do print(__name__)  - it will return __main__ if the same scripty containing it 
is directly executed.

Please complete this video - https://www.udemy.com/course/the-python-pro-course/learn/lecture/24248088#overview

for PEP8 guidelines

'''