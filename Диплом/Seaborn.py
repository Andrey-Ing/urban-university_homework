import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import my_datasets as md


def scatter(dataset=md.get_lissajous_figure()):
    data = pd.DataFrame({'x': dataset[0], 'y': dataset[1]})
    sns.scatterplot(data=data, x='x', y='y')
    plt.show()


#scatter()

def lineplot(dataset=md.get_pandas_dataframe()):
    data, name = dataset
    sns.set_theme(style="dark")
    line = sns.lineplot(data=data, x="Date", y="Price")
    line.set_title(name)
    x_index = range(1, len(data['Date']), 1000)
    # Убираем подписи осей
    plt.xticks(x_index, rotation=60)

    plt.yticks([])

    plt.tight_layout()
    plt.show()

#lineplot()


def bar_plot(dataset=md.get_github_list_data()):
    data, name = dataset
    sns.barplot(data=data, x='Week', y='Quantity', hue='Week').set_title(name)
    plt.xticks(rotation=10)

    plt.show()

bar_plot()
















