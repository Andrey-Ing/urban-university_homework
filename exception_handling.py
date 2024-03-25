def string_to_int(s):  # добавить обработку ValueError
    try:
        return int(s)
    except ValueError as exc:
        return f'Ошибка преобразования строки в число - {exc}'


print(string_to_int('42'))
print(string_to_int('5O'))  # в 50 ноль буква O


def read_file(filename):  # добавить обработку FileNotFoundError, IOError
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError as exc:
        return f'Файл не найден - {exc}'
    except IOError as exc:
        return f'Ошибка ввода-вывода - {exc}'


print(read_file('exception_handling.py'))
print(read_file('handl.py'))


def divide_numbers(a, b):  # добавить обработку ZeroDivisionError, TypeError
    try:
        return a / b
    except ZeroDivisionError as exc:
        return f'Попытка деления на ноль - {exc}'
    except TypeError as exc:
        return f'Ошибка в типах переменных - {exc}'


print(divide_numbers(7, 2.5))
print(divide_numbers(7, 0))
print(divide_numbers('hf', 8))


def access_list_element(lst, index):  # добавить обработку IndexError, TypeError
    try:
        return lst[index]
    except IndexError as exc:
        return f'Недопустимый индекс - {exc}'
    except TypeError as exc:
        return f'Передан не список - {exc}'


print(access_list_element([5, 6, 1, 2, 0], -2))
print(access_list_element([5, 6, 1, 2, 0], 54))
print(access_list_element(4367, 54))
