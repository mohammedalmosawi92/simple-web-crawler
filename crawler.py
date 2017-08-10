import requests
from bs4 import BeautifulSoup

def trade():
    #the url of the page you want to crawl
    url = "https://myanimelist.net/topanime.php"
    #get the whole page content with the header
    source_code = requests.get(url)
    #get hte whole page content without some stuff like the header
    text = source_code.text
    #convert the text to obj to sort or search through it
    soup = BeautifulSoup(text)
    for link in soup("a", {"class":"fw-b"}):
        #to get the value inside the a tag
        print(link.string)
        #to get the value of the attribute in the a tag
        print(link.get("href"))
trade()