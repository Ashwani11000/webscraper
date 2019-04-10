# To search for some topic and scraping the text, link, parent, children,
#  next siblings and some textual description of that link
from bs4 import BeautifulSoup
import requests


search = input("Search for:")
par = {"q": search}
r = requests.get("http://www.bing.com/search", params=par)

"""Here s is an object of Beautiful soup
html parser is a default parser then also we need to define it to prevent warning message"""
s = BeautifulSoup(r.text, "html.parser")
# only the items in ol tags having id b_results
results = s.find("ol", {"id": "b_results"})
# the items within ol inside the li tags having class b_algo
links = results.findAll("li", {"class": "b_algo"})

for item in links:
    item_text = item.find("a").text
    item_href = item.find("a").attrs["href"]
    # Checking that the text and link exists
    if item_href and item_text:
        print("TEXT:", item_text)
        print("LINKS:", item_href)

        # Checking for the parent of a tag
        print("parent:", item.find("a").parent)

        # Looking for the next sibling of h2 tag
        child1 = item.find("h2")
        print("next sibling of h2 is:", child1.next_sibling)

        # Printing all children of this item
        children = item.children
        for child in children:
            print("Child:", child)

        # For the textual description present in <p> tag
        print("\nSummary:", item.find("a").parent.parent.find("p").text)
