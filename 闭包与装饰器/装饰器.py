def decorator(func):
    print('start decorate')
    def wrapper():
        print('paint white')
        func()
        print('buy furniture')
        print('ending decorate')
    return wrapper
@decorator
def house():
    print('毛坯房')
house()

def house1():
    print('毛坯房2')
house1 = decorator(house1)
house1()

"""
带有参数的装饰器
"""
def decorator(func):
    print('start decorate')
    def wrapper(*args,**kwargs):
        print('paint white')
        func(args,kwargs)
        print('buy furniture')
        print('ending decorate')
    return wrapper
@decorator
def house(*args,**kwargs):
    print('毛坯房{},房龄为:{}'.format(*args,**kwargs))
house(30,age=70)



