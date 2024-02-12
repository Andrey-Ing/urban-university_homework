def print_params(a=1, b='строка', c=True):
    print(f'a = {a}, b = {b}, c = {c}')


print_params()
print_params(9)
print_params(b='Привет!')
print_params(c=False, b='Планета')

print_params(b=25)
print_params(c=[1, 2, 3])

values_list = ['Сфера', 3.27, (6, 8, 0)]
values_dict = {'a': 786, 'b': 'Аквариум', 'c': False}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['Телефон', 5886]
print_params(*values_list_2, 42)
