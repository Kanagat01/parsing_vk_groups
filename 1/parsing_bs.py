import requests
from bs4 import BeautifulSoup as BS 

selector_path = "#page_wrap > div > .scroll_fix > #page_layout > #page_body > #wrap3 > #content > \
                .wide_column_left > .wide_column_wrap > .wide_column > .page_block > #results"

titles = open('D:/IT/Заказы/Заполнить Excel таблицу группами VK.com по критериям/titles.txt', encoding='utf-8').read().split("\n")
cities = open('D:/IT/Заказы/Заполнить Excel таблицу группами VK.com по критериям/cities.txt', encoding='utf-8').read().split("\n")
for title in titles[10:]:
    for city in cities[430:]:
        print(title, city)
        r = requests.get(f"https://vk.com/groups?act=catalog&c%5Blike_hints%5D=1&c%5Bper_page%5D=40&c%5Bq%5D=40&c%5Bq%5D={title}%20{city}&c%5Bsection%5D=communities&c%5Bsort%5D=6&c%5Btype%5D=4&section%5D=communities")
        html = BS(r.content, "html.parser")
        input_tag = html.find_all(attrs={"class" : "groups_row search_row clear_fix"})
        elem1 = input_tag[0]['data-id']
        elem2 = input_tag[1]['data-id']
        elem3 = input_tag[2]['data-id']
        with open('D:/IT/Заказы/Заполнить Excel таблицу группами VK.com по критериям/id_s.txt', 'a', encoding='utf-8') as r:
            r.write(f"{elem1}, {elem2}, {elem3}\n")