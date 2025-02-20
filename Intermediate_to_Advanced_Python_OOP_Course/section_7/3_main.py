from random import randint
import turtle

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        if rectangle.point1.x < self.x < rectangle.point2.x \
                and rectangle.point1.y < self.y < rectangle.point2.y:
            return True
        else:
            return False


class Rectangle:

    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def area(self):
        return (self.point2.x - self.point1.x) * \
               (self.point2.y - self.point1.y)

''' 
We now need to modify this code to draw the rectangle

We can add draw method to rectangle class, but this would not be the best approach.

!! It is mostly not the best practice to modify your classes when you can extend them 
'''

class GuIRectangle(Rectangle): # -> GuIRectangle inherits from Rectangle so it will have
                                    #all the attributes and method of rectangle class

    def draw(self, canvas): # included canvas param as well, rather than call turtle module here
                            # it should be done in the main code and should have placeholder over here
        
        canvas.penup()

        if self.point1.x < self.point2.x:
            horizontal_length = self.point2.x - self.point1.x
            vertical_length = self.point2.y - self.point1.y
            canvas.goto(self.point1.x, self.point1.y)
            canvas.pendown()
            canvas.forward(horizontal_length)
            canvas.left(90)
            canvas.forward(vertical_length)
            canvas.left(90)
            canvas.forward(horizontal_length)
            canvas.left(90)
            canvas.forward(vertical_length)
            turtle.done()
            
        else:
            horizontal_length = self.point1.x - self.point2.x 
            vertical_length = self.point1.y - self.point2.y  
            myturtle.goto(self.point2.x, self.point2.y)
            myturtle.pendown()
            myturtle.forward(horizontal_length)
            myturtle.left(90)
            myturtle.forward(vertical_length)
            myturtle.left(90)
            myturtle.forward(horizontal_length)
            myturtle.left(90)
            myturtle.forward(vertical_length)
            turtle.done()

'''
This class addition is complete
'''

# Create rectangle object
# rectangle = Rectangle(Point(randint(0, 9), randint(0, 9)),
#               Point(randint(10, 19), randint(10, 19))) -> this is not needed now, we'll use GUIRectangle

gui_rectangle = GuIRectangle(Point(randint(0, 9), randint(0, 9)),
                             Point(randint(10, 19), randint(10, 19)))
# Print rectangle coordinates
print("Rectangle Coordinates: ",
      gui_rectangle.point1.x, ",",
      gui_rectangle.point1.y, "and",
      gui_rectangle.point2.x, ",",
      gui_rectangle.point2.y)

# Get point and area from user
user_point = Point(float(input("Guess x: ")), float(input("Guess y: ")))
user_area = float(input("Guess rectangle area: "))

# Print out the game result
print("Your point was inside rectangle: ", user_point.falls_in_rectangle(gui_rectangle))
print("Your area was off by: ", gui_rectangle.area() - user_area)

myturtle = turtle.Turtle()

gui_rectangle.draw(canvas=myturtle)



