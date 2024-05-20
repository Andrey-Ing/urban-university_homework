from requests import get
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


url = 'https://www.wikipedia.org'
response = get(url)
print(f'Дата и время на сервере {url} {response.headers['date']}')


X = np.random.randint(-100, 100, 30)
Y = np.random.randint(-100, 100, 30)


data = {'X': X, 'Y': Y}
participants = pd.DataFrame(data)
print(participants)


plt.scatter(X, Y, marker='*', color='green', alpha=0.6)
plt.title('График рассеяния')
plt.xlabel('X')
plt.ylabel('Y')

plt.show()
