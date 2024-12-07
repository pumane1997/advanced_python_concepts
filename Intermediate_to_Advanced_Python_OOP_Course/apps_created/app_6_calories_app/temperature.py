import requests
from selectorlib import Extractor

default_header = {
    'pragma' : 'no-cache',
    'cache-control' : 'no-cache',
    'dnt' : '1',
    'upgrade-insecure-requests' : '1',
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:117.0) Gecko/20100101 Firefox/117.0',
    'accept' : 'application/json, text/html;q=0.9, */*;q=0.8',
    'accept-language' : 'en-US,en;q=0.9,fr;q=0.8,es;q=0.7'
}

class TemperatureScrapper:
    ''' xx '''

    def __init__(self, city, country):
        self.city = city
        self.country = country

    def getTemperature(self, header = default_header):
        url = f'https://www.timeanddate.com/weather/{self.country}/{self.city}'
        request = requests.get(url, headers = header)
        extractor = Extractor.from_yaml_file('temperature.yaml')
        raw_temperature = extractor.extract(request.text)
        temperature = float(raw_temperature['temp'].replace("\xa0°C", ""))
        return temperature

pune_temp = TemperatureScrapper('Pune', 'India').getTemperature()
print(pune_temp)