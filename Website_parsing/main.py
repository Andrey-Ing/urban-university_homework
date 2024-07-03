import requests
from bs4 import BeautifulSoup, Comment
import re
import lxml

url = 'https://coinmarketcap.com'

# отправляем запрос с заголовками по нужному адресу
req = requests.get(url)
if req.status_code != 200:
    raise ConnectionError(f'Ответ от сайта {url} не 200 "OK"')
# считываем текст HTML-документа
src = req.text
#print(src)


#css_soup.select("p.strikeout.body")
# [<p class="body strikeout"></p>]
#<div class="sc-a093f09c-0 gPTgRa">
#sc-71024e3e-0 ehyBa-d
#span class="crypto-symbol"
# инициализируем html-код страницы
soup = BeautifulSoup(src, 'lxml')
#ii = soup.select("div.sc-a093f09c-0 gPTgRa")
#tr class="sc-240ce903-0 iPeVVh"
#selector = "tr.iPeVVh.sc-240ce903-0span, p.ehyBa-d.sc-71024e3e-0"
selector = "td"
#ii = soup.select(selector)

#ii = soup.find_all('a.span', class_='circle')


ii = soup.css.select('td > a > span.circle')

#ii = soup.css.select('div > table > tbody > tr > td')

#ii = soup.findAll('$')
print(len(ii))
# считываем заголовок страницы
res_str = ''
for i in ii:
    #print(i.parent.parent.parent.find(string=lambda text: isinstance(text, Comment)).parent)
    #print(i.parent.parent.parent.find_all('tr', string=re.compile('/d')))
    print(i.parent.parent.parent)
    #print(i.text)
    res_str += str(i) + '\n'
with open('test', 'w', newline='', encoding='utf-8') as file:
    file.write(res_str)

###
# < td > < b > Address: < / b > < / td >
# < td > My
# home
# address < / td >
# ###
#
# address = soup.find(text="Address:")
# b_tag = address.parent
# td_tag = b_tag.parent
# next_td_tag = td_tag.findNext('td')
# print
# next_td_tag.contents[0]
