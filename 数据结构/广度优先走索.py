from collections import deque


class Node(object):
    _name = deque()
    visited = deque()
    def __init__(self, value):
        self._value = value
        self._list = deque()

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._list.append(node)

    def __iter__(self):
        return iter(self._list)

    def depth_first(self):
        # print('yield begin')
        try:
            if self not in Node.visited:
                yield self
                Node.visited.append(self)
                # for t in self:
                yield from self.depth_first()

            elif self in Node.visited:
                for t in self:
                    yield from t.depth_first()

        except Exception as e:
            print(e)


# Example 一个需要注意的小地方是，如果你在迭代操作时不使用for循环语句，那么你得先调用 iter() 函数。
if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))
    #
    print(root)
    for ch in root.depth_first():
        print(ch)
