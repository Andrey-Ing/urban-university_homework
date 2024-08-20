import plotly.graph_objs as go
import plotly.express as px
import my_datasets as md


# минимальный код для отображения графиков
def scatter(dataset=md.get_lissajous_figure()):
    px.scatter(x=dataset[0], y=dataset[1]).show()


def line_plot(dataset=md.get_pandas_dataframe()):
    data, name = dataset
    fig = px.line(data, x="Date", y="Price", title=name, width=1800, height=1000)
    fig.show()


def bar_plot(dataset=md.get_github_list_data()):
    data, name = dataset
    fig = px.bar(data, x='Week', y='Quantity', title=name,
                 hover_data=['Week', 'Quantity'],
                 color='Week', )
    fig.show()


def scatter_3d(dataset=md.get_3d_data()):
    data, name = dataset
    x_grid, y_grid, z_grid = data

    fig = go.Figure(data=[go.Scatter3d(
        x=x_grid.flatten(),
        y=y_grid.flatten(),
        z=z_grid.flatten(),
        mode='markers',
        marker_colorscale='viridis',
        marker_color=z_grid.flatten(),
        marker=dict(
            size=2,
            opacity=0.8))])
    fig.add_annotation(dict(text=name, x=0.7, y=0.7, font_size=25, showarrow=False))
    fig.show()


# scatter()
# line_plot()
# bar_plot()
scatter_3d()
