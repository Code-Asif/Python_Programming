# to get the html data from any website
import requests

response = requests.get("https://www.codewithharry.com")
print(response.text)