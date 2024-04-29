# Задача 1: Фабрика Функций
def create_operation(operation):
    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiplication(x, y):
        return x * y

    def division(x, y):
        return x / y

    choice_dict = {'+': add, '-': subtract, '*': multiplication, '/': division}
    return choice_dict[operation]


my_func = create_operation('*')
print(my_func(7, 9))

my_func = create_operation('/')
print(my_func(7, 9))


# Задача 2: Лямбда-Функции
squaring = lambda x: x ** 2
print(squaring(5))


def squaring(x):
    return x ** 2


print(squaring(5))


# Задача 3: Вызываемые Объекты
class Rect:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        return self.a * self.b


area = Rect(11, 17)
print(area())
