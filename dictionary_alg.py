from tkinter import W
from urllib import request
from bs4 import BeautifulSoup as bs
import time
import requests

def writer():
    base_req = "https://www.bestwordlist.com/5letterwordspage"
    end = ".htm"
    list_pages = []
    
    for i in range(0,15):
        page = requests.get(base_req + str(i+1) + end)
        soup = bs(page.content, features="html.parser")
    page = requests.get("https://www.bestwordlist.com/5letterwords.htm")
    soup = bs(page.content, features="html.parser")
    a = soup.find_all(class_="mot")
    a += soup.find_all(class_="mot2")
    

    with open("word_list.txt", W) as f:
        for i in a:
            f.write(i.text)



    #button = soup.find()

if __name__== '__main__':
    writer()