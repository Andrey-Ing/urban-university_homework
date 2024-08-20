import requests
import numpy as np
import pandas as pd


def get_lissajous_figure():  # замкнутые траектории, прочерчиваемые точкой,
    # совершающей одновременно два гармонических колебания в двух взаимно перпендикулярных направлениях.
    t = np.linspace(0, 2 * np.pi, 200)
    return np.sin(5 * t), np.cos(4 * t)


def get_pandas_dataframe():  # Pandas Dataframe из csv файла
    return pd.read_csv('BrentOilPrices_from_www.kaggle.com.csv'), 'BrentOilPrices'


def get_github_list_data():  # получение списка последних коммитов в репозитории
    url = "https://api.github.com/repos/Andrey-Ing/urban-university_homework/stats/participation"
    req = requests.get(url).json()
    weeks = np.array(['seven weeks ago', 'six weeks ago', 'five weeks ago',
                      'four weeks ago', 'three weeks ago', 'two weeks ago', 'a week ago'])
    values_week = np.array(req['all'][-len(weeks)-1:-1])
    return {'Week': weeks, 'Quantity': values_week}, 'My Github commit count'


def get_3d_data():  # 3D цветок
    x = np.linspace(-20, 20, 200)
    y = np.linspace(-20, 20, 200)
    x_grid, y_grid = np.meshgrid(x, y)  # Матрица координат
    z_grid = np.sqrt(x_grid ** 2 + y_grid ** 2) + 3 * np.cos(np.sqrt(x_grid ** 2 + y_grid ** 2)) + 5
    return (x_grid, y_grid, z_grid), '3D flower'
