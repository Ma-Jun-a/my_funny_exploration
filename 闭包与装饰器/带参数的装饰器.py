import logging
from functools import wraps


def logged(level,name=None,message=None):

    def decorator(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__
        @wraps(func)
        def wrapper(*args,**kwargs):
            log.log(level,logmsg)
            return func(*args,**kwargs),message
        return wrapper
    return decorator

@logged(logging.DEBUG,message='func1')
def func1(x,y):
    re = x +y
    return re

@logged(logging.INFO,"example",message='func2')
def func2(x,y):
    re = x*y
    return re
print(func1(2,3))
print(func2(2,3))

