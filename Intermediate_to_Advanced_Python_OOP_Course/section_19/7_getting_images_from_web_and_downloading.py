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
import os
import time
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

'''
link = page.images[0]
# we need to create request object first
req = requests.get(link) # this is a response object (check with type)
# we an get content for this by content attribute
print(req.content) # in our case this is going to return bytes
# every type of file is represented by bytes in computers which basically some kind of very low level language.
# bytes are returned here because terminal is text absed interface
'''

def create_session_with_retries():
    session = requests.Session()
    retries = Retry(total=5, backoff_factor=0.5, status_forcelist=[429, 500, 502, 503, 504])
    session.mount("https://", HTTPAdapter(max_retries=retries))
    return session

download_path = './files'
search_query = 'beach'


try:
    # Search for the Wikipedia page
    page = wikipedia.page(search_query)
except wikipedia.exceptions.DisambiguationError as e:
    print(f"Disambiguation error: {e.options}")
except wikipedia.exceptions.PageError:
    print("Page not found.")

os.makedirs(download_path, exist_ok=True)

session = create_session_with_retries()

image_url = page.images[0]

if image_url.lower().endswith(('.jpg', '.jpeg', '.png')):
    try:
        # Set headers to avoid HTTP 403 errors
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
        }
        response = session.get(image_url, headers=headers)

        # Check if the request was successful
        if response.status_code == 200:
            # Save the image
            file_extension = image_url.split('.')[-1]
            file_name = f"{search_query.replace(' ', '_')}.{file_extension}"
            file_path = os.path.join(download_path, file_name)

            with open(file_path, 'wb') as file:
                file.write(response.content)

            print(f"Downloaded: {file_name}")
        else:
            print(f"Failed to retrieve image from {image_url}. Status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while downloading {image_url}: {e}")
else:
    print(f"Skipped non-JPG/PNG image: {image_url}")