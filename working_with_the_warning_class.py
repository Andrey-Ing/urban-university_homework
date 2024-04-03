import warnings
from warnings import simplefilter


def division(a, b):
    if abs(b) < 0.01:
        warnings.warn(f'Осторожно, знаменатель слишком близок к нулю ({b})')
    return a / b


my_a = 10
my_b = 0.001


print('simplefilter = error')
simplefilter('error')
try:
    print(division(my_a, my_b))
except UserWarning as exc:
    print(f'Перехватил пользовательское исключение: {exc}')

print('simplefilter = always')
simplefilter('always')
print(division(my_a, my_b))

print('simplefilter = ignore')
simplefilter('ignore')
print(division(my_a, my_b))
