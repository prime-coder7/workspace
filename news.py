import requests
import json 

query = input("What type of news are you interested in? ")

url = f"https://newsapi.org/v2/everything?q={query}&from=2024-11-05&sortBy=publishedAt&apiKey=56e818fd8692475f9f7ab618adca50cc"

r = requests.get(url)

news = json.loads(r.text)

# print(news, type(news))

for articles in news["articles"]:
    print(articles["title"])
    print(articles["description"])
    print("--------------------------------------")

