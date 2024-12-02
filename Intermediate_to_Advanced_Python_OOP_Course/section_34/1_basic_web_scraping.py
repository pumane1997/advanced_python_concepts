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

print(pprint(request.content))