# -*- coding:utf-8 -*-

from pluggy import PluginManager, HookspecMarker, HookimplMarker

hookspec = HookspecMarker("myPluggyDemo_5")
hookimpl = HookimplMarker("myPluggyDemo_5")


class HookSpec:
    @hookspec
    def calculate(self, a, b):
        pass


class HookImpl1:
    @hookimpl
    def calculate(self, a, b):
        print('HookImpl1 execute!')
        return a + b


class HookImpl2:
    @hookimpl(tryfirst=True)
    def calculate(self, a, b):
        print('HookImpl2 execute!')
        return a * b


class WrapperPluggy:
    @hookimpl(hookwrapper=True)
    def calculate(self, a, b):
        print('WrapperPluggy execute!')
        print("Before yield")
        result = yield            #此处返回的值为其他两个pluggy执行的结果
        print("After yield,result is {result.get_result()}")
        return a * b + (a + b)


pm = PluginManager("myPluggyDemo_5")
pm.add_hookspecs(HookSpec)
pm.register(HookImpl1())
pm.register(HookImpl2())
pm.register(WrapperPluggy())
print(pm.hook.calculate(a=2, b=3))
