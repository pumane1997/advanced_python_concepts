import numpy as np
from PIL import Image

class Canvas():
    '''
    This class represents the canvas
    '''

    def __init__(self, color, height, width):
        self.height = height
        self.width = width
        self.color = color

    def draw(self):
        data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        data[:] = [self.color[0], self.color[1], self.color[2]]
        return data
    
    def make(self, data):
        img = Image.fromarray(data, f'{'rgb'.upper()}')
        img.save('./files/canvas.png')

class Square():
    '''
    This class represents the square
    '''

    def __init__(self, x, y, color, side):
        self.x = x
        self.y = y
        self.color = color
        self.side = side

    def draw(self, data):
        #data = canvas.draw()
        data[self.x:self.x+self.side , self.y:self.y+self.side] = [self.color[0], self.color[1], self.color[2]]
        return data


class Rectangle():
    '''
    This class represents the square
    '''

    def __init__(self, x, y, color, height, width):
        self.x = x
        self.y = y
        self.color = color
        self.height = height
        self.width = width

    def draw(self, data):
        #data = canvas.draw()
        data[self.x:self.x+self.width , self.y:self.y+self.height] = [self.color[0], self.color[1], self.color[2]]
        return data