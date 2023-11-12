# Read news with the help of newsapi
import requests
import json

query = input("What type of news are you interested in? ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2023-10-12&sortBy=publishedAt&apiKey=0179cf39fae3425f886c07831c107dfd"

r = requests.get(url)
news = json.loads(r.text)
# print(news, type(news))
for article in news["articles"]:
    print(f"{i}.Title: ", end=" ")
    print(article["title"])
    print("Description: ", end=" ")
    print(article["description"])
    print("--------------------------------------------------------")