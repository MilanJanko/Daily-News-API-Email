import requests
from send_email import send_email

api_key = 'd5305f54a6e44a398ed98e785f3bb424'
url = ('https://newsapi.org/v2/everything?'
       'q=tesla&from=2023-07-14&sortBy=publishedAt&'
       'apiKey=d5305f54a6e44a398ed98e785f3bb424')

# Create request
request = requests.get(url)

# Get json object with data
content = request.json()

# Check content data
body = ''
for article in content['articles']:
    if article['title'] is not None:
        body = body + article['title'] + '\n' + article['description'] + 2*'\n'

# Create a regular email
message = f"""\
Subject: Test email from Daily News

{body}
"""
# Encoding email since I got error in converting ASCII
message = message.encode('utf-8')
send_email(message)
