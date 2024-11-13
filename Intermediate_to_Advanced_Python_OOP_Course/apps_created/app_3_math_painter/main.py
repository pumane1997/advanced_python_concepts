# The code can be refactored for square class and rectangle class draw method to directly
# refer to canvas object rather than data. You can drop draw method of canvas and implement canvas
# initiation in __init__ method.

import shapes

'''
Testing with manual values

canvas = shapes.Canvas((255, 255, 255), 10, 10)
square = shapes.Square(2, 1, (255, 0, 0), 3)
rectangle = shapes.Rectangle(5, 5, (0, 255, 0), 2, 1)
data = canvas.draw()
data = square.draw(data=data)
data = rectangle.draw(data=data)
canvas.make(data)
'''

# Take inputs for canvas
canvas_width = int(input('Enter canvas width: '))
canvas_height = int(input('Enter canvas height: '))
canvas_color = tuple(map(int, input('Enter canvas color as three comma-separated values (e.g., 255,255,255): ').split(',')))
canvas = shapes.Canvas(canvas_color, canvas_height, canvas_width)
data = canvas.draw()

while True:
    user_input = input('What would you like to draw? Enter quit to quit: ')
    if user_input == 'quit':
        break
    elif user_input == 'rectangle':
        # Take inputs for rectangle
        x = int(input('Enter x of rectangle: '))
        y = int(input('Enter y of rectangle: '))
        width = int(input('Enter width of rectangle: '))
        height = int(input('Enter height of rectangle: '))
        color = tuple(map(int, input('Enter color of rectangle as three comma-separated values (e.g., 255,0,0): ').split(',')))
        rectangle = shapes.Rectangle(x, y, color, height, width)
        data = rectangle.draw(data=data)
    elif user_input == 'square':
        # Take inputs for square
        x = int(input('Enter x of square: '))
        y = int(input('Enter y of square: '))
        side = int(input('Enter side of square: '))
        color = tuple(map(int, input('Enter color of square as three comma-separated values (e.g., 0,0,255): ').split(',')))
        square = shapes.Square(x, y, color, side)
        data = square.draw(data=data)

canvas.make(data)