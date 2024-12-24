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

    def _buil_url(self): # this is a private method and is not meant to be used outside of the class
        url = self.base_url+ \
              f"qInTitle={self.interests}&"+ \
              f"from={self.from_date}&"+ \
              f"to={self.to_date}&"+ \
              f"language={self.language}&"+ \
              f"apiKey={self.api_key}"
        return url

    def _get_article(self):
        url = self._buil_url()
        response = requests.get(url)
        content = response.json()
        articles = content['articles']

    def get(self):
        # created separate method for building url & getting article from url
        # as there is a lot going on in this method
        email_body = ''
        for article in articles:
            email_body = email_body + article['title'] + "\n" + article['url'] + "\n\n"
        return email_body