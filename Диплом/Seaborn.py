import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# sns.set_theme(style="ticks")
#
# df = sns.load_dataset("penguins")
# sns.pairplot(df, hue="species")
# plt.show()


t = np.linspace(0, 2 * np.pi, 10000)

sns.lineplot(x=np.sin(2 * t), y=np.cos(3 * t))
plt.show()


