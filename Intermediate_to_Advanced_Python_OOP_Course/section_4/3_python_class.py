
# Creating Class

class Point:   # Senctence case for single word, CamelCase for multiple (_ style for functions)
               # good practice to leave one line here
    def __init__(self, x, y):             # special function for declaring params - these params are actually instance variables
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

'''
What is self?

self in a class is the variable that holds the object instance that is being created 
by the class
'''

print(point1.x)

print(Point(3,9).x)


'''
self can be any name - but obv you use self
In self.<var>, <var> can be anything and not necessarily the param values, but we keep it 
consistent 
'''

class Point:  
               
    def __init__(this_object, x, y):         
        this_object.a = x 
        this_object.b = y
        #print(x, y)
        

print(Point(3,9).b)


'''
Class methods
'''

print('john'.count('j'))

'''
In above line, 'john' is a string type object and essentially an object instance of
string class (inbuilt)

This object has a method - count (and a lot of others)

As you can see, methodss are what make objects useful

We have __init__ method in our class, but this is a special method -> it does not
return anything & it's meant to initialize the objects you are creating.

Now lets modify our point class to add a method that checks if given point falls in 
the rectangle
'''

class Point:  
               
    def __init__(self, x, y):         
        self.x = x 
        self.y = y
        
    def falls_in_rectangle(self, lowleft, upright):                # self has to be the first arg for every method
        if (lowleft[0] < self.x < upright[0]) and ((lowleft[1] < self.y < upright[1])):
            return True
        else:
            return False
        

lowleft = [2, 4]
upright = [6, 10]
print(Point(3, 5).falls_in_rectangle(lowleft, upright))


'''
__init__ method vs normal methods

'''

class Point:  
               
    def __init__(self, x, y):     
        print('Hey, I am __init__ method')    
        self.x = x 
        self.y = y
        
    def falls_in_rectangle(self, lowleft, upright):
        print('Hey, I am ordinary method')                
        if (lowleft[0] < self.x < upright[0]) and ((lowleft[1] < self.y < upright[1])):
            return True
        else:
            return False
        

pointX = Point(1,2) 

# this statement prints - 'Hey, I am __init__ method' immediately on instansiating
# the other print statement will only be executed on calling that method explicitly


'''
Add a new distance method to the Point class. The method should calculate the distance from the 
coordinates of the current point (i.e., the self.x and self.y coordinates) to the coordinates of any 
other given point, and such coordinates can be provided as x and y arguments to the distance method.
'''

class Point:  
               
    def __init__(self, x, y):     
        self.x = x 
        self.y = y
        
    def falls_in_rectangle(self, lowleft, upright):                
        if (lowleft[0] < self.x < upright[0]) and ((lowleft[1] < self.y < upright[1])):
            return True
        else:
            return False
        
    def caculate_distance(self, coordinates): # this will take list/tuple of co-ordinates
        import math
        distance = math.sqrt((abs(self.x-coordinates[0])**2) \
                             +(abs(self.y-coordinates[1])**2))
        return distance
    
    def caculate_distance_from_point(self, point): # this will take point object as arg
        import math
        distance = math.sqrt((abs(self.x-point.x)**2) \
                             +(abs(self.y-point.y)**2))
        return distance
    

print(Point(3, 5).caculate_distance([18, 20]))

point2 = Point(18, 20)

print(Point(3, 5).caculate_distance_from_point(point2))