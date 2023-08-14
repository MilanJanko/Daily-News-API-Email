import requests

api_key = 'd5305f54a6e44a398ed98e785f3bb424'
url = ('https://newsapi.org/v2/everything?'
       'q=tesla&from=2023-07-14&sortBy=publishedAt&'
       'apiKey=d5305f54a6e44a398ed98e785f3bb424')

# Create request
request = requests.get(url)

# Get json object with data
content = request.json()

# Check content data
for article in content['articles']:
    print(article['title'])
