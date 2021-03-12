
def ood(n):
    my_list = []
    m = 0
    k = 0
    for i in range(n):
        if i == m:
            k += 1
            m = k * 2 +1
            my_list.append(i)
    return my_list[-1]
# print(ood(1000))
def fun(m):
    k = 0
    while True:
        k1 = m - (k * 2 + 1)
        k += 1
        if k1 > 0:
            continue
        else:
            return k

# print(fun(100))

def back1(n):
    x = ood(n)
    y = n - x
    print(x)
    k = 0
    z = 1
    for i in range(fun(x)):
        k += 1
        s = k*2 - 1
        if x < s:
            return
        else:
            x = x - s
            print(x,s)
        #记录行数
        z = z + 1
        print(" "*z+"*"*s+" "*z,end='\n')

    print(y)
# back1(10)


