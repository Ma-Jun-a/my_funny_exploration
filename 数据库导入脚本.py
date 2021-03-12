class A:
    attr = 'A'
class B(A):
    pass
class C(A):
    attr = 'C'
class D(B,C):
    pass
a = A()
b = B()
c = C()
d = D()
print(a.attr)
print(b.attr)
print(c.attr)
print(d.attr)