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

    def area(self):
        area = (self.upright.x - self.lowleft.x)* \
        (self.upright.y - self.lowleft.y)
        return area    
    

print(Rectangle(Point(2, 3), Point(12, 18)).area())


# rather than having coordinates as low left and up right, it could just
# point 1 and point 2.