import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import lxml
import time

url = 'https://coinmarketcap.com/en/'

# Заголовки, чтобы замаскироваться под браузер
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
    "Connection": "keep-alive",
    "Host": "coinmarketcap.com",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0"
}

# отправляем запрос с заголовками по нужному адресу
req = requests.get(url, headers)
if req.status_code != 200:
    raise ConnectionError(f'Ответ от сайта {url} не 200 "OK"')
# считываем текст HTML-документа
src = req.text
#print(src)


options = webdriver.FirefoxOptions()
#options.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0")


try:
    driver = webdriver.Firefox(
        #executable_path= r"C:\Program Files\Mozilla Firefox\firefox.exe",
        options=options
    )

    driver.get(url=url)
    print(driver.page_source)
    with open("index_selenium", "w") as file:
        file.write(driver.page_source)

except Exception as ex:
    print(ex)
finally:
    pass
   # driver.close()
   # driver.quit()





#css_soup.select("p.strikeout.body")
# [<p class="body strikeout"></p>]
#<div class="sc-a093f09c-0 gPTgRa">
#sc-71024e3e-0 ehyBa-d
#span class="crypto-symbol"
# инициализируем html-код страницы
soup = BeautifulSoup(driver.page_source, 'lxml')
#ii = soup.select("div.sc-a093f09c-0 gPTgRa")
#tr class="sc-240ce903-0 iPeVVh"
ii = soup.select("tr.iPeVVh.sc-240ce903-0span, p.ehyBa-d.sc-71024e3e-0")
print(len(ii))
# считываем заголовок страницы
for i in ii:
    print(i.text)
with open('test', 'w', newline='', encoding='utf-8') as file:
    file.write(soup.prettify())
# Программа выведет: Курсы - Блог компании Селектел
