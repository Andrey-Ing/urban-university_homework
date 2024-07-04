import csv
import requests
from bs4 import BeautifulSoup
import lxml
import re
import time


def write_cmc_top():
    url = 'https://coinmarketcap.com'
    # отправляем запрос с заголовками по нужному адресу
    req = requests.get(url)
    if req.status_code != 200:
        raise ConnectionError(f'Ответ от сайта {url} не 200 "OK"')

    src = req.text

    first_part_name = []
    first_part_money = []
    second_part_name = []
    second_part_money = []

    # для проверки данных после парсинга
    first_part_len = 10
    second_part_len = 90

    soup = BeautifulSoup(src, 'lxml')
    # На сайте первые 10 значений имени и цены берутся по первым селекторам
    first_part_name_select = soup.css.select('div > div > p.ehyBa-d')
    first_part_money_select = soup.css.select('td > div.gPTgRa')
    # Остальные 90 значений имени и цены берутся по второму селектору имени из которого потом получим и цену
    second_part_name_select = soup.css.select('td > a > span.circle')

    for name in first_part_name_select:
        first_part_name.append(name.text)

    for money in first_part_money_select:
        first_part_money.append(float(money.text.lstrip('$').replace(',', '')))

    for name in second_part_name_select:
        second_part_name.append(name.next_element.text)
        second_part_money.append(float(name.parent.parent.parent.find(string=re.compile(r'\d'))))

    # проверка данных
    if (len(first_part_name) == len(first_part_money) == first_part_len) and \
            (len(second_part_name) == len(second_part_money) == second_part_len):
        pass
    else:
        raise ValueError(f'Ошибка в парсинге данных')

    total_market_capitalization = 0.0

    for value in first_part_money:
        total_market_capitalization += value

    for value in second_part_money:
        total_market_capitalization += value

    # время - для названия файла
    current_time = time.time()
    local_time = time.localtime(current_time)
    formatted_time = time.strftime("%H.%M %d.%m.%Y", local_time)

    with open(f'{formatted_time}.csv', 'w', newline='') as csvfile:
        fieldnames = ['Name', 'MC', 'MP']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=' ')

        writer.writeheader()

        for i in range(len(first_part_name)):
            writer.writerow({'Name': first_part_name[i], 'MC': first_part_money[i],
                             'MP': round(first_part_money[i] / total_market_capitalization * 100, 1)})

        for i in range(len(second_part_name)):
            writer.writerow({'Name': second_part_name[i], 'MC': second_part_money[i],
                             'MP': round(second_part_money[i] / total_market_capitalization * 100, 1)})


write_cmc_top()
