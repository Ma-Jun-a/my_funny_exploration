#
def ood(n):
    my_list = []
    m = 0
    k = 0
    for i in range(n):
        if i == m:
            k += 1
            m = k * 2 +1
            my_list.append(i)
    return my_list
print(ood(1000))