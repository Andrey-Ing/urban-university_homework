import requests
from bs4 import BeautifulSoup
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
ii = soup.select(selector)
#ii = soup.findAll('$')
print(len(ii))
# считываем заголовок страницы
res_str = ''
for i in ii:
    print(i.text)
    res_str += str(i)+'\n'
with open('test', 'w', newline='', encoding='utf-8') as file:
    file.write(res_str)
# Программа выведет: Курсы - Блог компании Селектел
