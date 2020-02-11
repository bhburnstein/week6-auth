import requests
import secrets

base_url = 'https://newsapi.org/v2/top-headlines'
params = {
    "apiKey": secrets.NEWSAPI_KEY,
    "country": "us",
    "q": "new hampshire"
}

response = requests.get(base_url, params)
result = response.json()
#print(result)

#print(result['articles'])

for article in result['articles']:
    #print(f"{article['source']['name']}")
    print(f"{article['title']}")