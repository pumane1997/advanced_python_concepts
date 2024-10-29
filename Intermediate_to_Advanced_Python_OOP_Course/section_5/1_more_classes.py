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
        self.lowleft = lowleft      # these will hold point objects 
        self.upright = upright

rectanglex = Rectangle(Point(5,6), Point(7,9))

pointx = Point(4, 8)

print(pointx.falls_in_rectangle(rectanglex))