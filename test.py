import requests
from bs4 import BeautifulSoup

import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def convert(lst):
    return ' '.join(lst).split()

URL = "https://en.wikipedia.org/wiki/Something_(Beatles_song)"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find_all()
elements = {'title':[],'h1':[], 'h2':[], 'p':[]}
words = []

stop_words = set(stopwords.words('english'))

for tag in elements:
    for result in results: 
        if result.find(tag):
            w = word_tokenize(result.find(tag).text)
            for x in w:
                if x not in stop_words:
                    words += convert([result.find(tag).text])

words.sort()
words_df = pd.DataFrame(words)[0]
final = words_df.value_counts()

for w,k in final.items():
    print(f"{w}: {k}")

