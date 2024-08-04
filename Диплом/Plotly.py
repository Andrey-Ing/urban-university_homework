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



t = np.linspace(0, 2 * np.pi, 1000)

#px.scatter(x=np.sin(2 * t), y=np.cos(3 * t)).show()

fig = go.Figure()
fig.add_trace(go.Scatter(x=np.sin(2 * t), y=np.cos(3 * t)))
fig.show()






