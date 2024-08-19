import plotly

import plotly.graph_objs as go

import plotly.express as px

from plotly.subplots import make_subplots

import numpy as np

import pandas as pd

# x = np.arange(0, 5, 0.1)
# def f(x):
#     return x**2
#
# px.scatter(x=x, y=f(x)).show()


# t = np.linspace(0, 2 * np.pi, 1000)
#
# #px.scatter(x=np.sin(2 * t), y=np.cos(3 * t)).show()
#
# fig = go.Figure()
# fig.add_trace(go.Scatter(x=np.sin(2 * t), y=np.cos(3 * t)))
# fig.show()

import plotly.graph_objects as go
import my_datasets as md


# def grid_to_list3d(x_grid, y_grid, z_grid):
#     x_list = x_grid.flatten()
#     y_list = y_grid.flatten()
#     z_list = z_grid.flatten()
#     return x_list, y_list, z_list
#
#
#
#
# # x_grid, y_grid, z_grid = md.get_3d_data()
# # fig = go.Figure(data=[go.Scatter3d(
# #     x=x_grid.flatten(),
# #     y=y_grid.flatten(),
# #     z=z_grid.flatten(),
# #     mode='markers',
# #     marker=dict(
# #         size=2,
# #         color='peru',  # set color to an array/list of desired values
# #         opacity=0.8))])  # прозрачность
# # print(x_grid.shape)
# # #fig = px.scatter_3d(x=x_grid, y=y_grid, z=z_grid)
# # fig.show()
#
#
# import my_datasets as md
# data = md.get_pandas_dataframe()
#
# import plotly.express as px
# fig = px.line(data_frame=data, x='Date', y='Price', title='Apple Share Prices over time (2014)')
# fig.show()


def scatter(dataset=md.get_lissajous_figure()):
    px.scatter(x=dataset[0], y=dataset[1]).show()


# scatter()


def lineplot(dataset=md.get_pandas_dataframe()):
    data, name = dataset
    fig = px.line(data, x="Date", y="Price", title=name, width=1800, height=1000)
    fig.show()


# lineplot()


def bar_plot(dataset=md.get_github_list_data()):
    data, name = dataset
    fig = px.bar(data, x='Week', y='Quantity', title=name,
                 hover_data=['Week', 'Quantity'],
                 color='Week',)
    fig.show()


bar_plot()
