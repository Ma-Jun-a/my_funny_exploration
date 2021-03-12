from functools import wraps


def outer(**kwargs):
    def decorator(func):
        @wraps(func)
        def wrapper(*args):
            func(*args)
            print('装饰功能执行{time}次'.format(**kwargs))
        return wrapper
    return decorator

@outer(time=100)
def house(n):
    print('这是一座{}年的老房子'.format(n))

house(70)
print(house)

