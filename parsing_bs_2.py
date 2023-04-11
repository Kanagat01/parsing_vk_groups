import requests
from bs4 import BeautifulSoup as BS 


titles = open('D:\IT\Orders\Parsing VK/titles_2.txt', encoding='utf-8').read().split("\n")
cities = open('D:\IT\Orders\Parsing VK/cities_2.txt', encoding='utf-8').read().split("\n")
for city in cities:
    elems = []
    for title in titles:
        r = requests.get(f"https://vk.com/groups?act=catalog&c%5Blike_hints%5D=1&c%5Bper_page%5D=40&c%5Bq%5D=40&c%5Bq%5D={city}%20{title}&c%5Bsection%5D=communities&c%5Bsort%5D=6&c%5Btype%5D=4&section%5D=communities")
        html = BS(r.content, "html.parser")
        a = html.select("#results > div > div.info > div.labeled.title.verified_label > a", limit=10)
        for x in a:
            if (title.lower() in x.text.lower()) and (city.lower() in x.text.lower()):
                id = x.parent.parent.parent["data-id"]
                if id not in elems:
                    elems.append(id)
                    break
    with open('D:\IT\Orders\Parsing VK/id_s_2.txt', 'a', encoding='utf-8') as r:
        elems = ', '.join(elems)
        print(f"{city}: {elems}")
        r.write(f"{city}:{elems}\n")
