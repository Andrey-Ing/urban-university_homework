from requests import get
import numpy as np
import matplotlib.pyplot as plt


url = 'https://www.wikipedia.org'
response = get(url)
print(f'Дата и время на сервере {url} {response.headers['date']}')


X = np.random.randint(-100, 100, 1000)
Y = np.random.randint(-100, 100, 1000)

plt.scatter(X, Y, marker='*', color='green', alpha=0.6)
plt.title('График рассеяния')
plt.xlabel('X')
plt.ylabel('Y')

plt.show()






