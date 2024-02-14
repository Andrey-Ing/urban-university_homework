def test(*args, **kwargs):
    print(f'args  {args}\nkwargs  {kwargs}')


test(57, 'Hello', True, param_1=765, param_2='UTT')


def factorial(n):
    if n > 0:
        return n * factorial(n-1)
    elif n == 0:
        return 1
    else:
        return None


print(factorial(5))
