import requests
from pprint import pprint

''' 
Web scraping

To scrape data from web, we need two inputs
 - web url
 - html tag where the desired data is located 

'''

url = 'https://www.timeanddate.com/weather/india/pune'

# we will create a request and store it in the variable

request = requests.get(url) # get is method of requests class & it expects url as input

# print(request)

# <Response [200]> means that the request was successful

'''
sometimes the websites make it difficult for scripts to scrape the data, but there 
is a technique to make script (Python) behave like a browser - making the request using headers
as an argument which is supposed to be a dict containing the browser header 
'''

header = {
    'pragma' : 'no-cache',
    'cache-control' : 'no-cache',
    'dnt' : '1',
    'upgrade-insecure-requests' : '1',
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:117.0) Gecko/20100101 Firefox/117.0',
    'accept' : 'application/json, text/html;q=0.9, */*;q=0.8',
    'accept-language' : 'en-US,en;q=0.9,fr;q=0.8,es;q=0.7'
}

request = requests.get(url, headers = header)

print(request)

# print(request.content)
 
# this will give you all the html content of url
# the output will be ugly, if you want it to bi in better format, use pprint

# print(pprint(request.content))
# above will give you slightly better formatted content

#
'''
- The content attribute of requests is generally used when you want to extract files,
pdf content, images etc. But in case we want to extract some text/numbers form web page, 
we use text attribute
content attribute returns byte type data
text attribute returns string
'''

# print(request.text)

# we will use selector lib to extract temperature from the text

from selectorlib import Extractor

# Extractor is the class that contains the methods we need for extraction

extractor = Extractor.from_yaml_file('temperature.yaml')

''' 
In above line of code, we are instansiating the Extractor class. We do it differently than
usual method - by calling a method of it. You don't always initialize the class using ()
after class name, but also by a method that initializes the class.

The way we extract by this way is - 
    - Create a yaml file in root dir (preferably)
    - Add this ->
        temp:
            xpath: ''
    - the xpath should be identifier of the value we want to extract. find it on the webpage
    - provide this yaml file's path to - Extractor.from_yaml_file() and execute

This creates teh extractor object
'''

print(extractor)

# print(extractor.extract(request.text))

raw_temp = extractor.extract(request.text)

temp = float(raw_temp['temp'].replace("\xa0°C", ""))

print(temp)