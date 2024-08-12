import numpy as np
import matplotlib.pyplot as plt
import my_datasets as md

#
# t = np.linspace(0, 2 * np.pi, 1000)
# plt.figure(figsize=(4,4))
# plt.plot(np.sin(5 * t), np.cos(4 * t))
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
#
# ##
#


# fig = plt.figure(figsize=(20, 12))
# ax_3d = fig.add_subplot(projection='3d')
# x_grid, y_grid, z_grid = md.get_3d_data()
# # ax_3d.plot_wireframe(x_grid, y_grid, z_grid) # строит каркасную сетку
# ax_3d.scatter(x_grid, y_grid, z_grid, s=2, c='r')  # строит на основе точек
# # ax_3d.plot_surface(x_grid, y_grid, z_grid, cmap='viridis') # строит поверхность
# ax_3d.set_xlabel('x'), ax_3d.set_ylabel('y'), ax_3d.set_zlabel('z')
# plt.show()


import my_datasets as md
data = md.get_pandas_dataframe()

# plotting a bar graph
#data.plot(x='Date', y='Price', kind="bar")


# plotting a histogram
plt.plot(data['Price'])
plt.show()

#print(data[0:10]['Date'])





