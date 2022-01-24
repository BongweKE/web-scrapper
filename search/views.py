from re import search
from django.shortcuts import render

from .forms import searchForm ,saveForm
from .models import Search
# the views exported to urls.py
# HistoryView, SearchView

# url parsing imports
import requests
from bs4 import BeautifulSoup
# imports to count words etc
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# function to convert sentence to list
def convert(lst):
    return ' '.join(lst).split()

def HistoryView(request):
    #view for search history saved to sqlite DB
    search = Search.objects.all()
    return render(request, "history.html", {'searches': search})

def SearchView(request):
    if request.method == "POST":
        form = searchForm(request.POST)
        if form.is_valid():
            myUrl = form.cleaned_data['url']
            page = requests.get(myUrl)

            soup = BeautifulSoup(page.content, "html.parser")
            results = soup.find_all()
            elements = {'title':[],'h1':[], 'h2':[], 'p':[], 'buttons':[]}
            words = []
            # stop words are words that shouldn't be counted
            stop_words = set(stopwords.words('english'))
            # all tags we've chosen above
            for tag in elements:
                # we have a lot of results from beautiful soup
                for result in results: 
                    # if we have that tag
                    if result.find(tag):
                        # tokenize the words so it is similar 
                        w = word_tokenize(result.find(tag).text)
                        # if they are not stpo words we save it to  our word list
                        for x in w:
                            if x not in stop_words:
                                words += convert([result.find(tag).text])
            # sort the array
            words.sort()
            # convert to a pandas df
            words_df = pd.DataFrame(words)[0]
            # get simple stats from pandas
            final_df = words_df.value_counts()
            wordList = []
            for w,k in final_df.items():
                wordList += [[w,k]]
            
            #now we create data for our form so a user can save it to the DB
            default_data = {'results': wordList, 'website': myUrl}
            form = saveForm(default_data, auto_id=False)
            return render(request, "search_results.html", {'df':wordList, 'url':myUrl })
    # if request.GET.get('url') == "True":
    #     #save to database
    #     form = saveForm(request.GET)
    #     if form.is_valid():
    #         myUrl = form.cleaned_data['url']
    #         df = form.cleaned_data['df']
    #         s = Search(website=myUrl,results=df)
    #         s.save()
    #         return render(request, "success.html", {})
    else:
        form = searchForm()
        return render(request, "search.html", {'form': form})
