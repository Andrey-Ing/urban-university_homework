import requests
import numpy as np
import pandas as pd

from pprint import pprint as pp


def get_lissajous_figure():
    t = np.linspace(0, 2 * np.pi, 200)
    return np.sin(5 * t), np.cos(4 * t)


def get_pandas_dataframe():
    return pd.read_csv('BrentOilPrices_from_www.kaggle.com.csv'), 'BrentOilPrices'


def get_github_list_data():
    url = "https://api.github.com/repos/Andrey-Ing/urban-university_homework/stats/participation"
    req = requests.get(url).json()
    weeks = np.array(['seven weeks ago', 'six weeks ago', 'five weeks ago',
                      'four weeks ago', 'three weeks ago', 'two weeks ago', 'a week ago'])
    values_week = np.array(req['all'][-len(weeks)-1:-1])
    return {'Week': weeks, 'Quantity': values_week}, 'My Github commit count'

def get_3d_data():
    # Генерируем данные
    x = np.linspace(-20, 20, 100)
    y = np.linspace(-20, 20, 100)
    x_grid, y_grid = np.meshgrid(x, y)
    z_grid = np.sqrt(x_grid ** 2 + y_grid ** 2) + 3 * np.cos(np.sqrt(x_grid ** 2 + y_grid ** 2)) + 5
    return x_grid, y_grid, z_grid
