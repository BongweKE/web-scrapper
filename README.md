## A webscrapper 

- when fed a url  this app will give text of what the app is about and other basic commands. 
- requirements.txt file will outline what we will need to run this app.

use $ python -m pip install -r requirements.txt


# How the user uses the app.

- run the django app then input a url in the given textbox
- the web app will output a list of words with wordcount in the given website, arranged in descending order \
	from the most common  word to the least common one
- you better have an internet connection or just input a local website
 **beware of copyright infringement if you scrape websites you don't have enough info on**


# how it works
when you input the url of the website;
1. django python sends a POST request which is first validated.
2. Using beautifulSoup, we get the website content
3. we decided to only take 'title','h1', 'h2','p', & 'button' elements since they are the most common ones
4. we loop over all the results checking if they are any of the above chosen elements
5. sentences are converted to words using word_tokenize function
6. we add all the words to a list which is sorted before pandas converts it to a dataframe
7. pandas value_counts() is used to count ocurrences of unique words before sorting in order of the most common to the least common word
8. the results are rendered in tabular format\

*future improvements*\
We will be able to save to the database and compare different search results using python DS tools

# how to setup the environment
*this is more suitable for a linux user*\
1. Set up a virtual environment\
$ python3 -m venv envName

Once the process is complete, you also need to activate the virtual environment:\
(this is the first command for when you've already setup the venv)\

$ source envName/bin/activate

2. Install Django if you dont have it (or update)\
(envName) $ python -m pip install django

3. pull the repo from github and note the location of the requirements.txt file\
(envName) $ python -m pip install -r webScrapper/requirements.txt

4. now that you have all the requirements you can run the program from within the directory\
(envName) $ cd ./webScrapper\
(envName) $ python manage.py migrate\
(envName) $ python manage.py runserver

5. You'll get a link which you can copy and run in the browser. \
if yours is anything like mine copy and paste http://127.0.0.1:8000/ in your favorite browser\
make sure the internet connection is on so you can find the website to scrape\
make sure you install the requirep python packages in requirements.txt


## HAVE FUN 


