'''
How to build this program without going through all the intermediate 
steps (CLI only program)

1. Just write the classes (objects) with __init__ method

2. Write the class methods

'''

class Point:  
               
    def __init__(self, x, y):     
        self.x = x 
        self.y = y
        
    def falls_in_rectangle(self, rectangle):                
        if (rectangle.lowleft.x < self.x < rectangle.upright.x) \
            and ((rectangle.lowleft.y < self.y < rectangle.upright.y)):
            return True
        else:
            return False


class Rectangle:

    def __init__(self, lowleft, upright):
        self.lowleft = lowleft     
        self.upright = upright

# create rectangle randomly

from random import randint

rectangle = Rectangle(
    Point(randint(0,9), randint(0,9)),
    Point(randint(10,19), randint(10,19))
)

print("Rectangle Co-ordinates: ",
      rectangle.lowleft.x, ",",
      rectangle.lowleft.y, "and",
      rectangle.upright.x, ",",
      rectangle.upright.y)

user_point = Point(float(input("Guess X: ")),
                   float(input("Guess Y: ")))

print('Result: ', user_point.falls_in_rectangle(rectangle))