import requests
from pprint import pprint as pp


def get_usd():
    url = " https://api.github.com/repos/Andrey-Ing/urban-university_homework/commits?path=/"
    r = requests.get(url).json()
    rate_dict = (r["payload"]["rates"]) #получаем массив rates, который содержит всё что нам надо
    def has_sale(string): #здесь я пытался вытянуть значение sell, но вытянул все словари, которые содержат значение sell
        return "sell" in string

    l = list(filter(has_sale, rate_dict))

    print(l)

url = ("https://api.github.com/repos/Andrey-Ing/urban-university_homework/stats/participation")
#r = requests.get(url).json()
r = requests.get(url).json()
#pp(r[29])

pp(sum(r['all']))




