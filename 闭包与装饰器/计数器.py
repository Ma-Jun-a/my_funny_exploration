def generator_counter():
    container = [0]
    def counter():
        container[0] = container[0]+ 1
        print('计数器的计数为{}次'.format(container[0]))
    return counter
counter = generator_counter()
def counter_set(n):
    i = 0
    while i < n:
        counter()
        i +=1
counter_set(60)


