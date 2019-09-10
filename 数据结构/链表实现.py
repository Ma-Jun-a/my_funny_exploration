#线性表的顺序存储实现也就是列表的方法来实现。
#链表只是逻辑上相连的线性

class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.next = None

class SingleLinkList(object):
    def __init__(self, node=None):
        self._head = node

    def is_empty(self):
        return self._head == None

    def length(self):
        cur = self._head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self._head
        while cur != None:
            print(cur.elem, end='')
            cur = cur.next
        print('\n')

    def add(self, item):
        node = Node(item)
        node.next = self._head
        self._head = node

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next  != None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        if pos <=0:
            self.add(item)
        elif pos > self.length() - 1:
            self.append(item)
        else:
            per = self._head
            count = 0
            while count < pos -1:
                count += 1
                per = per.next
            node = Node(item)
            node.next = per.next
            per.next = node

    def remove(self, item):
        cur = self._head
        pre = None
        while cur != None:
            if cur.elem == item:
                return  True
            else:
                cur = cur.next
        return False

if __name__ == '__main__':
    node = Node(100)


