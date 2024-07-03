import csv

import requests
from bs4 import BeautifulSoup, Comment
import re
import lxml

url = 'https://coinmarketcap.com'

# отправляем запрос с заголовками по нужному адресу
req = requests.get(url)
if req.status_code != 200:
    raise ConnectionError(f'Ответ от сайта {url} не 200 "OK"')

src = req.text

first_part_len = 10
second_part_len = 90

first_part_name = ['tt']
first_part_money = []
second_part_name = []
second_part_money = []

soup = BeautifulSoup(src, 'lxml')

first_part_name_select = soup.css.select('div > div > p.ehyBa-d')
first_part_money_select = soup.css.select('td > div.gPTgRa')

second_part_name_select = soup.css.select('td > a > span.circle')

for name in first_part_name_select:
    first_part_name.append(name.text)

for money in first_part_money_select:
    first_part_money.append(float(money.text.lstrip('$').replace(',', '')))

for name in second_part_name_select:
    second_part_name.append(name.next_element.text)
    second_part_money.append(name.parent.parent.parent.find(string=re.compile(r'\d')))

if (len(first_part_name) != len(first_part_money) != first_part_len) or \
        (len(second_part_name) != len(second_part_money) != second_part_len):
    raise ValueError(f'Ошибка в парсинге данных')


print(len(first_part_name))


with open('names.csv', 'w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})

# #ii = soup.css.select('div > table > tbody > tr > td')
#
# #ii = soup.findAll('$')
# print(len(ii))
# # считываем заголовок страницы
# res_str = ''
# for i in ii:
#     #print(i.parent.parent.parent.find(string=lambda text: isinstance(text, Comment)).parent)
#     print(i.parent.parent.parent.find(string=re.compile(r'\d')))
#     #print(i.parent.parent.parent)
#     #print(i.text)
#     res_str += str(i) + '\n'
# with open('test', 'w', newline='', encoding='utf-8') as file:
#     file.write(res_str)
#
# ###
# # < td > < b > Address: < / b > < / td >
# # < td > My
# # home
# # address < / td >
# # ###
# #
# # address = soup.find(text="Address:")
# # b_tag = address.parent
# # td_tag = b_tag.parent
# # next_td_tag = td_tag.findNext('td')
# # print
# # next_td_tag.contents[0]
