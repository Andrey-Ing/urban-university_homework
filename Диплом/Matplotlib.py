import calendar
import locale
locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
import numpy as np
import matplotlib.pyplot as plt
import my_datasets as md


#
# t = np.linspace(0, 2 * np.pi, 100)
# plt.figure(figsize=(4,4))
# plt.scatter(np.sin(5 * t), np.cos(4 * t))
# plt.show()
# for i in range(1000000):
#     print(i)
# ##
# x = np.linspace(0, 4 * np.pi, 100)
# ##
# plt.figure()
# plt.plot(x, np.sin(x), 'r-')
# plt.plot(x, np.cos(x), 'b--')
# plt.show()
# for i in range(1000000):
#     print(i)
# #
# # ##
# #
#
#
# # fig = plt.figure(figsize=(20, 12))
# # ax_3d = fig.add_subplot(projection='3d')
# # x_grid, y_grid, z_grid = md.get_3d_data()
# # # ax_3d.plot_wireframe(x_grid, y_grid, z_grid) # строит каркасную сетку
# # ax_3d.scatter(x_grid, y_grid, z_grid, s=2, c='r')  # строит на основе точек
# # # ax_3d.plot_surface(x_grid, y_grid, z_grid, cmap='viridis') # строит поверхность
# # ax_3d.set_xlabel('x'), ax_3d.set_ylabel('y'), ax_3d.set_zlabel('z')
# # plt.show()
#
#
# # import my_datasets as md
# # data = md.get_pandas_dataframe()
# #
# # # plotting a bar graph
# # #data.plot(x='Date', y='Price', kind="bar")
# #
# #
# # # plotting a histogram
# # plt.plot(data['Price'])
# # plt.show()
# #
# # #print(data[0:10]['Date'])


def scatter(dataset=md.get_lissajous_figure()):
    plt.scatter(x=dataset[0], y=dataset[1])
    plt.show()


#scatter()

def bar(dataset=md.get_github_list_data()):
    #plt.style.use('_mpl-gallery')
    # plot:
    print(dataset)
    fig, ax = plt.subplots()
    months = list(calendar.month_name)[1:]  # делаем срез т.к. первый месяц в списке пустой
    print(months)
    ax.hist(x=dataset, edgecolor="white")
    #
    # ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
    #        ylim=(0, 56), yticks=np.linspace(0, 56, 9))

    plt.show()

#bar()


#
#     print(dataset)
#     plt.bar(x=dataset[0], height=dataset[1])
#     plt.show()
#
#
# plt.style.use('_mpl-gallery')
#
# # make data:
# x = 0.5 + np.arange(8)
# y = [4.8, 5.5, 3.5, 4.6, 6.5, 6.6, 2.6, 3.0]
#
# # plot
# fig, ax = plt.subplots()
#
# ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)
#
# ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
#        ylim=(0, 8), yticks=np.arange(1, 8))
#
# plt.show()



#bar()

def lineplot(dataset=md.get_pandas_dataframe()):
    data, name = dataset
    fig, ax = plt.subplots()
    plt.gcf().set_size_inches(15, 10)
    ax.plot(data['Date'], data['Price'])
    ax.set_title(name)
    x_index = range(1, len(data['Date']), 1000)
    # Убираем подписи осей
    plt.xticks(x_index, rotation=60)

    plt.show()

#lineplot()


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

bar_plot()







