import requests

class Newsfeed:
    '''
    Representing multiple news titles and links as a single string
    '''

    base_url = "http://newsapi.org/v2/everything?"
    api_key = "82871d18df4441e09a08f20f5e74ac3a"

    def __init__(self, interests, from_date, to_date, language='en'):
        self.interests = interests
        self.from_date = from_date
        self.to_date = to_date
        self.language = language

    def get(self):
        url = self.base_url+f"qInTitle={self.interests}&"+f"from={self.from_date}&"+"to={self.to_date}&"+f"language={self.language}&"+f"apiKey={self.api_key}"
        response = requests.get(url)
        content = response.json()
        articles = content['articles']
        email_body = ''
        for article in articles:
            email_body = email_body + article['title'] + "\n" + article['url'] + "\n\n"
        return email_body