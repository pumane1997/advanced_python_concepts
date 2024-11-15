'''
import wikipedia
import requests
import os

def download_images_from_wikipedia(search_query, download_path="images"):
    # Search for the Wikipedia page
    page = wikipedia.page(search_query)
    
    # Make a directory to store images
    os.makedirs(download_path, exist_ok=True)
    
    # Loop over images in the page and download each one
    for index, image_url in enumerate(page.images):
        # Get only .jpg and .png images (skip SVGs and other types if any)
        if image_url.lower().endswith(('.jpg', '.jpeg', '.png')):
            try:
                # Set headers to avoid HTTP 403 errors
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
                }
                response = requests.get(image_url, headers=headers)
                
                # Check if the request was successful
                if response.status_code == 200:
                    # Save the image
                    file_extension = image_url.split('.')[-1]
                    file_name = f"{search_query.replace(' ', '_')}_{index}.{file_extension}"
                    file_path = os.path.join(download_path, file_name)
                    
                    with open(file_path, 'wb') as file:
                        file.write(response.content)
                    
                    print(f"Downloaded: {file_name}")
                else:
                    print(f"Failed to retrieve image from {image_url}. Status code: {response.status_code}")
            
            except Exception as e:
                print(f"An error occurred while downloading {image_url}: {e}")
        else:
            print(f"Skipped non-JPG/PNG image: {image_url}")

# Example usage:
download_images_from_wikipedia("War")
'''

import wikipedia
import requests
import os
import time
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

def create_session_with_retries():
    session = requests.Session()
    retries = Retry(total=5, backoff_factor=0.5, status_forcelist=[429, 500, 502, 503, 504])
    session.mount("https://", HTTPAdapter(max_retries=retries))
    return session

def download_images_from_wikipedia(search_query, download_path="images"):
    try:
        # Search for the Wikipedia page
        page = wikipedia.page(search_query)
    except wikipedia.exceptions.DisambiguationError as e:
        print(f"Disambiguation error: {e.options}")
        return
    except wikipedia.exceptions.PageError:
        print("Page not found.")
        return

    # Make a directory to store images
    os.makedirs(download_path, exist_ok=True)

    # Create a session with retries
    session = create_session_with_retries()

    # Loop over images in the page and download each one
    for index, image_url in enumerate(page.images):
        # Filter for .jpg and .png images
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
                    file_name = f"{search_query.replace(' ', '_')}_{index}.{file_extension}"
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

# Example usage:
download_images_from_wikipedia("War")
