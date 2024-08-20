import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import my_datasets as md


# минимальный код для отображения графиков
def scatter(dataset=md.get_lissajous_figure()):
    data = pd.DataFrame({'x': dataset[0], 'y': dataset[1]})
    sns.scatterplot(data=data, x='x', y='y')
    plt.show()


def line_plot(dataset=md.get_pandas_dataframe()):
    data, name = dataset
    sns.set_theme(style="dark")
    line = sns.lineplot(data=data, x="Date", y="Price")
    line.set_title(name)
    # прореживаем подписи на оси X
    x_index = range(1, len(data['Date']), 1000)
    plt.xticks(x_index, rotation=60)

    plt.tight_layout()  # настраивает отступы
    plt.show()


def bar_plot(dataset=md.get_github_list_data()):
    data, name = dataset
    sns.barplot(data=data, x='Week', y='Quantity', hue='Week').set_title(name)
    plt.xticks(rotation=10)

    plt.show()


def joint_grid(dataset=md.get_3d_data()):
    data, name = dataset
    x_grid, y_grid, z_grid = data

    df = pd.DataFrame({
        'X': x_grid.flatten(), 'Y': y_grid.flatten(), 'Z': z_grid.flatten()})

    sns.set_theme(style='darkgrid')

    g = sns.JointGrid(data=df, x='X', y='Z', hue='X')
    g.plot(sns.scatterplot, sns.histplot)
    g.fig.suptitle(f'{name} to show the joint grid')

    plt.show()

# scatter()
# line_plot()
# bar_plot()
# joint_grid()
