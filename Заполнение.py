import pandas as pd

data_frame = {}
cities = open('D:\IT\Orders\Parsing VK\cities_2.txt', encoding='utf-8').read().split("\n")
data_frame['Город'] = cities

# titles = open('D:/IT/Заказы/Заполнить Excel таблицу группами VK.com по критериям/titles.txt', encoding='utf-8').read().split("\n")
id_s = open('D:\IT\Orders\Parsing VK\id_s_2.txt', encoding='utf-8').read().split("\n")

# for idx, title in enumerate(titles):
#     i = idx * 500
#     data_frame[title] = id_s[i:i+500]

for i in range(len(id_s)):
    id_s[i] = id_s[i].split(":")[1]

data_frame['ID групп'] = id_s
df = pd.DataFrame(data_frame)
df.to_excel('D:/IT/Orders/Parsing VK/table_2.xlsx')