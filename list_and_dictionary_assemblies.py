given = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]


def odd(number):
    return number % 2


def square(number):
    return number ** 2


filter_odd = filter(odd, given)
map_square = map(square, filter_odd)

print(list(map_square))
