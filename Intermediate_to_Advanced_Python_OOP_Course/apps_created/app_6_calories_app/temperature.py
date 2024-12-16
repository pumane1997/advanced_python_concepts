import requests
from selectorlib import Extractor

default_header = { # this should be a class parameter (including base url & yaml path)
    'pragma' : 'no-cache',
    'cache-control' : 'no-cache',
    'dnt' : '1',
    'upgrade-insecure-requests' : '1',
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:117.0) Gecko/20100101 Firefox/117.0',
    'accept' : 'application/json, text/html;q=0.9, */*;q=0.8',
    'accept-language' : 'en-US,en;q=0.9,fr;q=0.8,es;q=0.7'
}

'''
Ideal way to structure this class (suggested in tutorial)

- def __init__
- def _build_url -> returns url
- def _scrape -> scrapes temp
- def get -> cleans and returns temp
''' 

class TemperatureScrapper:
    ''' xx '''

    def __init__(self, city, country):
        self.city = city.replace(' ', '-')
        self.country = country.replace(' ', '-')

    def getTemperature(self, header = default_header):
        try:
            url = f'https://www.timeanddate.com/weather/{self.country}/{self.city}'
            request = requests.get(url, headers = header)
            extractor = Extractor.from_yaml_file('temperature.yaml')
            raw_temperature = extractor.extract(request.text)
            temperature = float(raw_temperature['temp'].replace("\xa0°C", ""))
        except AttributeError as e:
            print("No temperature was returned. Setting temperature to 15", e)
            temperature = 15
        else:
            print("Both values were valid.")
        
        return temperature

# pune_temp = TemperatureScrapper('Pune', 'India').getTemperature()
# print(str(pune_temp) +' : Todays Tempreature')