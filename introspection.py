def introspection_info(obj):
    info = dict()

    if hasattr(obj, '__name__'):
        info['name'] = obj.__name__

    if hasattr(obj, '__module__'):
        info['module'] = obj.__module__

    info['type'] = type(obj)
    info['callable'] = callable(obj)
    info['attributes'] = dir(obj)

    return info


def my_function():
    pass


class MyClass:
    pass


a = 9.25424
b = 'string'
c = my_function
d = MyClass()


print(introspection_info(a), '\n',
      introspection_info(b), '\n',
      introspection_info(c), '\n',
      introspection_info(d),)

