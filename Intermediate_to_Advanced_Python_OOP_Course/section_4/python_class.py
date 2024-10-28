
# Creating Class

class Point:   # Senctence case for single word, CamelCase for multiple (_ style for functions)
               # good practice to leave one line here
    def __init__(self, x, y):             # special function for declaring params
        self.x = x
        self.y = x
        

point1 = Point(10, 20)

print(point1) # ---> <__main__.Point object at 0x0000016792273080>

'''
The word __main__ in the output above is name of the current script (more accurately,
the script where class Point is defined). If this were defined in another file, lets say
geometry.py, it would show output as geometry.Point

Note that no prefix would be there for builtin classes
'''

# Lets modify class Point so it prints coordindates on printing point object

# class Point:   
               
#     def __init__(self, x, y):             
#         self.x = x
#         self.y = x


