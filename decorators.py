from math import sqrt


def determ_prime(number):
    # список простых чисел начинается с 2, всё остальное можно сразу отмести
    if number <= 1:
        return False
    number_sqrt = int(sqrt(number))
    divisors = range(2, (number_sqrt + 1))
    # Если число не простое, то в отрезке от 1 до квадратного корня числа, точно будут его делители.
    for element in divisors:
        if number % element == 0:
            return False
    return True


def is_prime(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        if determ_prime(res):
            print("Простое")
        else:
            print("Составное")
        return res
    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)
