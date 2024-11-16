import wikipedia
import requests
import os
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

import warnings
from bs4 import GuessedAtParserWarning
warnings.filterwarnings("ignore", category=GuessedAtParserWarning)

def create_session_with_retries():
    session = requests.Session()
    retries = Retry(total=5, backoff_factor=0.5, status_forcelist=[429, 500, 502, 503, 504])
    session.mount("https://", HTTPAdapter(max_retries=retries))
    return session

def get_resolved_page(search_query: str):
    try:
        # Attempt to fetch the exact page
        page = wikipedia.page(search_query)
        return page
    except wikipedia.exceptions.DisambiguationError as e:
        print(f"Disambiguation error: {e.options}")
        print("Refining the search using the first valid option...")
        # Use the first valid search result
        search_results = wikipedia.search(search_query)
        if search_results:  
            for result in search_results:
                try:
                    page = wikipedia.page(result)
                    return page
                except wikipedia.exceptions.DisambiguationError:
                    continue  # Skip ambiguous pages
                except wikipedia.exceptions.PageError:
                    continue  # Skip invalid pages
        print("Failed to resolve the disambiguation.")
    except wikipedia.exceptions.PageError:
        print("Page not found.")
    return None

def download_image(search_query: str, download_path: str = './files') -> None:
    
    os.makedirs(download_path, exist_ok=True)
    page = get_resolved_page(search_query)

    if not page:
        print("Failed to retrieve the page.")
        return  

    session = create_session_with_retries()

    if page.images:

        for image_url in page.images:

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
                        file_name = 'current_image.jpg'
                        file_path = os.path.join(download_path, file_name)

                        with open(file_path, 'wb') as file:
                            file.write(response.content)

                        print(f"Downloaded: {file_name}")
                        break
                    else:
                        print(f"Failed to retrieve image from {image_url}. Status code: {response.status_code}")

                except requests.exceptions.RequestException as e:
                    print(f"An error occurred while downloading {image_url}: {e}")
            else:
                    print(f"Skipped non-JPG/PNG image: {image_url}")

    else:   
            print("No images found on the page.")


#download_image('moon')        