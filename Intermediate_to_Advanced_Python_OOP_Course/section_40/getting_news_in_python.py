# API key - 82871d18df4441e09a08f20f5e74ac3a

from newsapi import NewsApiClient
from rich import print_json
import json
import requests
import pprint

# Init
newsapi2 = NewsApiClient(api_key='82871d18df4441e09a08f20f5e74ac3a')

# /v2/top-headlines
top_headlines = newsapi2.get_top_headlines(#q='politics',
                                          sources='bbc-news,the-verge'
                                          #,
                                          #category='business',
                                          #language='en',
                                          #country='us'
                                          )
# print(top_headlines)
# print_json(data=json.dumps(top_headlines))

# /v2/everything
# all_articles = newsapi.get_everything(q='bitcoin',
#                                       sources='bbc-news,the-verge',
#                                       domains='bbc.co.uk,techcrunch.com',
#                                       from_param='2017-12-01',
#                                       to='2017-12-12',
#                                       language='en',
#                                       sort_by='relevancy',
#                                       page=2)
#print(all_articles)

# /v2/top-headlines/sources
# sources = newsapi.get_sources()
#print(sources)


# another way to get the api response

url = "http://newsapi.org/v2/everything?" \
"qInTitle=nasa&" \
"from=2024-12-22&" \
"sortBy=publishedAt&" \
"language=en&" \
"apiKey=82871d18df4441e09a08f20f5e74ac3a"

response = requests.get(url)

content = response.text
# pprint.pprint(content)

# text is not the best way to extract this data - its good when we are scraping html content
# we should use json() for api response

content = response.json()
pprint.pprint(content['articles'][0]['title'])
# ['title']
