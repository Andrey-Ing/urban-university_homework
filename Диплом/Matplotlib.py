import matplotlib.pyplot as plt
import my_datasets as md


# минимальный код для отображения графиков
def scatter(dataset=md.get_lissajous_figure()):
    plt.scatter(x=dataset[0], y=dataset[1])
    plt.show()


def line_plot(dataset=md.get_pandas_dataframe()):
    data, name = dataset
    fig, ax = plt.subplots()
    plt.gcf().set_size_inches(15, 10)
    ax.plot(data['Date'], data['Price'])
    ax.set_title(name)
    # прореживаем подписи на оси X
    x_index = range(1, len(data['Date']), 1000)
    plt.xticks(x_index, rotation=60)

    plt.show()


def bar_plot(dataset=md.get_github_list_data()):
    data, name = dataset
    fig, ax = plt.subplots()
    plt.gcf().set_size_inches(6, 8)
    bar_labels = data['Week']
    bar_colors = ['tab:orange', 'tab:red', 'tab:blue', 'tab:green', 'tab:purple']
    ax.bar(data['Week'], data['Quantity'], label=bar_labels, color=bar_colors)

    ax.set_ylabel('Week')
    ax.set_title(name)
    ax.legend()
    plt.xticks(rotation=15)

    plt.show()


def scatter_3d(dataset=md.get_3d_data()):
    data, name = dataset
    x_grid, y_grid, z_grid = data

    fig = plt.figure(figsize=(20, 12))
    ax_3d = fig.add_subplot(projection='3d')

    # ax_3d.plot_wireframe(x_grid, y_grid, z_grid) # строит каркасную сетку
    # ax_3d.scatter(x_grid, y_grid, z_grid, s=2, c='r')  # строит на основе точек
    ax_3d.plot_surface(x_grid, y_grid, z_grid, cmap='viridis')  # строит поверхность
    ax_3d.set_xlabel('x'), ax_3d.set_ylabel('y'), ax_3d.set_zlabel('z')
    ax_3d.set_title(name)
    plt.show()


# scatter()
# line_plot()
# bar_plot()
scatter_3d()
