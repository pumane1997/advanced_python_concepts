import numpy as np
from PIL import Image, ImageDraw, ImageFont
'''
images are pixels and pixels are numbers
'''

data = np.zeros((5, 4, 3), dtype=np.uint8)
data[:] = [255, 255, 0]
print(data)

# Make a red patch
data[1:3] = [255, 0, 0] # makes a horizontal red patch as we are accessing rows

# Make a red patch
data[: , 1:3] = [255, 0, 0] # makes a vertical red patch as we are accessing columns

img = Image.fromarray(data, f'{'rgb'.upper()}')
#img.save('canvas.png')