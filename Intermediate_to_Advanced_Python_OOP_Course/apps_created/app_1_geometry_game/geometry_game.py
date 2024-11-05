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

class GuIPoint(Point):

    def draw(self, canvas, size=5, color="red"):
        if canvas.isdown():
            canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size, color)

class Rectangle:

    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def area(self):
        return (self.point2.x - self.point1.x) * \
               (self.point2.y - self.point1.y)

class GuIRectangle(Rectangle): 

    def draw(self, canvas): 
        
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


gui_rectangle = GuIRectangle(Point(randint(0, 100), randint(0, 100)),
                             Point(randint(0, 100), randint(0, 100)))
# Print rectangle coordinates
print("Rectangle Coordinates: ",
      gui_rectangle.point1.x, ",",
      gui_rectangle.point1.y, "and",
      gui_rectangle.point2.x, ",",
      gui_rectangle.point2.y)

# Get point and area from user
user_point = GuIPoint(float(input("Guess x: ")), float(input("Guess y: ")))
user_area = float(input("Guess rectangle area: "))

# Print out the game result
print("Your point was inside rectangle: ", user_point.falls_in_rectangle(gui_rectangle))
print("Your area was off by: ", gui_rectangle.area() - user_area)

myturtle = turtle.Turtle()

gui_rectangle.draw(canvas=myturtle)

user_point.draw(canvas=myturtle)

turtle.done()