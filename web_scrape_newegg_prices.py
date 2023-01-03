import re

import requests
from bs4 import BeautifulSoup

search_term = input("what product do y ou want to search for? ")

url = f"https://www.newegg.com/p/pl?N=4131&d={search_term}"

web_page = requests.get(url).text

doc = BeautifulSoup(web_page, "html.parser")

page_ammount_text = doc.find(class_="list-tool-pagination-text").strong.text

page_ammount = int(page_ammount_text[page_ammount_text.index('/') + 1:])


def get_price(item_link):
    item_container = item_link.find_parent(class_="item-container")
    price_tag = item_container.find(class_="price-current")
    if price_tag.strong:
        price_dollars = price_tag.strong.text.replace(',', '')
        price_cents = price_tag.sup.text
        price = float(price_dollars) + \
            float(price_cents)  # dollars + cents
        return price
    else:
        return None


items = []
for page_index in range(1, page_ammount + 1):
    url = f"https://www.newegg.com/p/pl?N=4131&d={search_term}&page={page_index}"
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")

    item_links = doc.find_all(class_="item-title",
                              text=re.compile(search_term))
    for item_link in item_links:
        if get_price(item_link):
            items.append(item_link)

items.sort(key=lambda x: get_price(x))

for item in items:
    print(item.text)
    print(f"Price: {get_price(item)}")
    print(item['href'])
    print("---------------------------------------------------")
