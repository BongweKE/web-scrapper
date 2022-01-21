import requests
from bs4 import BeautifulSoup

URL = "https://oxylabs.io/blog/python-web-scraping"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find_all()
elements = {'h1':[], 'h2':[] }
for element in results:
    if element.find("h1"):
        elements['h1'] += [element.find("h1").text]
    if element.find("h2"):
        elements['h2'] += [element.find("h2").text]

print(elements)