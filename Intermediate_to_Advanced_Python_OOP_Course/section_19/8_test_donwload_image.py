import wikipedia
import requests

'''
# Fetch the Wikipedia page
page = wikipedia.page('war')

# Filter to get only URLs that end with common image file extensions
image_urls = [img for img in page.images if img.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]

if image_urls:
    # Take the first image that is in a proper format
    image_url = image_urls[0]
    print(f"Image URL: {image_url}")

    # Download the image
    req = requests.get(image_url)

    # Check if the request was successful
    if req.status_code == 200:
        with open('war_2.jpg', 'wb') as file:
            file.write(req.content)
        print("Image saved as war.jpg")
    else:
        print("Failed to retrieve the image")
else:
    print("No suitable images found.")
'''


import requests

# Define the title of the Wikipedia page
title = "War"

# Step 1: Get the JSON response from the Wikipedia API for the page
response = requests.get(
    f"https://en.wikipedia.org/w/api.php?action=query&titles={title}&prop=images&format=json"
)

# Check if the response is successful
if response.status_code != 200:
    print(f"Failed to fetch page data. Status code: {response.status_code}")
else:
    data = response.json()
    page_id = list(data["query"]["pages"].keys())[0]
    images = data["query"]["pages"][page_id].get("images", [])

    # Step 2: Filter to get URLs that end with common image formats
    image_titles = [img["title"] for img in images if img["title"].lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]

    if image_titles:
        # Use the title of the first suitable image to get its direct URL
        image_title = image_titles[0]
        print(f"Attempting to fetch image: {image_title}")

        # Step 3: Fetch direct URL of the image
        image_info_response = requests.get(
            f"https://en.wikipedia.org/w/api.php?action=query&titles={image_title}&prop=imageinfo&iiprop=url&format=json"
        )

        # Check if the response is successful
        if image_info_response.status_code != 200:
            print(f"Failed to fetch image info. Status code: {image_info_response.status_code}")
        else:
            image_info_data = image_info_response.json()
            image_page_id = list(image_info_data["query"]["pages"].keys())[0]
            image_info = image_info_data["query"]["pages"][image_page_id].get("imageinfo", [])

            if image_info:
                image_url = image_info[0]["url"]
                print(f"Image URL: {image_url}")

                # Step 4: Download the image from the direct URL
                image_req = requests.get(image_url)

                if image_req.status_code == 200:
                    with open('war.jpg', 'wb') as file:
                        file.write(image_req.content)
                    print("Image saved as war.jpg")
                else:
                    print(f"Failed to retrieve the image content. Status code: {image_req.status_code}")
            else:
                print("No image info available. The image might be restricted or unavailable.")
    else:
        print("No suitable images found on the page.")


# Step 4: Download the image from the direct URL with headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}
image_req = requests.get(image_url, headers=headers)

if image_req.status_code == 200:
    with open('war.jpg', 'wb') as file:
        file.write(image_req.content)
    print("Image saved as war.jpg")
else:
    print(f"Failed to retrieve the image content. Status code: {image_req.status_code}")
