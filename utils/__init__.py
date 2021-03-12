class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(str(self._children))

# Example
if __name__ == '__main__':
    root = Node(0)
    # print(root)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)

    # Outputs Node(1), Node(2)
    for ch in root:
        print(ch)

# 如果你想实现一种新的迭代模式，使用一个生成器函数来定义它。 下面是一个生产某个范围内浮点数的生成器：
def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment