class C(object):
    def __init__(self):
        print('class c')
    def __call__(self, *args, **kwargs):
        pass

print('__init__.py')