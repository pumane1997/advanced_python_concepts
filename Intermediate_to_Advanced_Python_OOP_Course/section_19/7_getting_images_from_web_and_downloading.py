# We will use wikipedia library for getting images from web

import wikipedia

page = wikipedia.page('war') 
# page is the function/method of wikipedia library. It gets search query as an input
# This way we can explore wikipedia by python
# print(type(page))
# print(dir(page)) # this gives available attributes of wiki page
# print(page.summary)
# print(page.images) # This will give you the link of the image
# print(len(page.images))
# print(page.images[0])

# we will use requests library to download the image from the link
import requests

# Filter to get only URLs that end with common image file extensions
image_urls = [img for img in page.images if img.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.svg'))]

# Set headers to avoid HTTP 403 errors
headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
            }

response = requests.get(image_urls[0], headers=headers)


'''
link = page.images[0]
# we need to create request object first
req = requests.get(link) # this is a response object (check with type)
# we an get content for this by content attribute
print(req.content) # in our case this is going to return bytes
# every type of file is represented by bytes in computers which basically some kind of very low level language.
# bytes are returned here because terminal is text absed interface
'''
# to view this as an image, we need to save this byte data as a file 

with open('war.jpg', 'wb') as file:
    file.write(response.content)