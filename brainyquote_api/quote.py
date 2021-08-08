# THIS IS USED FOR EDUCATIONAL ONLY. PLEASE READ THE TERMS OF SERVICE OF BRAINYQUOTE AT https://www.brainyquote.com/about/terms FOR MORE INFORMATION

import re
import requests
import random
from bs4 import BeautifulSoup

def category():
        category_list = [] # Full list of categories on the brainyquotes webiste.

        category_url = 'http://www.brainyquote.com/quotes/topics.html'
        html = requests.get(category_url)
        soup = BeautifulSoup(html.text, "html.parser")

        category = soup.find_all('a', {"href": re.compile("/topics/")}) # Retrieves all code on the website with a reference to /topics/{TOPIC}
        for i in category:
            category_list.append(i.text.strip()) # Iterates through the list and strips everything except for the topic name
        return category_list

def quoteCall(category, maxpage):
    while True:
        page = random.randint(0, maxpage) # Randomises a number between 0 and the specified maximum page the user wants the scraper to go through
        url = f"http://www.brainyquote.com/quotes/topics/{category}_{page}.html"
        html = requests.get(url)
        soup = BeautifulSoup(html.text, features="html.parser")


        for div in soup.find_all("div", {"class": "qbn-box"}): # Iterates through all code on the website with class of "qbn box" since it usually contains keywords that are already in the code and messes it up
            div.decompose()
        for div in soup.find_all("div", {"class": "kw-box"}): # Same as code above except its with class of "kw-box"
            div.decompose()

        divID = f"pos_{str(page)}_{random.randint(0,100)}" # Retrieves all code that contains quotes, hence the pos_ at the beginning specifying the position of each quote on the webpage
        find = soup.find("div", {"id": divID})
        if find != None and find != "" and find != " ": # If the returned string is not empty - since sometimes the retrieved quote doesn't come back properly
            quote = ""                                  # - then the whole loop is iterated through again to find another quote
            quote += find.text.replace("\n\n\n\n", "\n")
            return quote
            break

if __name__ == "__main__":
    # Example of this module in use.
    print(f"This is a tool used to scrape the brainyquote.com page for quotes based on the specified category. "
           "It returns a randomised quote based on the maximum page you want the scraping tool to go through.")
    print(f"An example of this tool in action would be this")
    quote = quoteCall(category()[79], 3)
    print(f"This is a quote from the category {category()[79]}:  {quote}")