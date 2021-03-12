class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 1.1建立空表。
        temp1, temp2 = [], []
        # 1.1设置与l1,l2相同的两个链表(optional)。
        f1, f2 = l1, l2
        # 1.2用while循环把节点值填充至List。
        while f1:
            temp1.append(f1.val)
            f1 = f1.next
        while f2:
            temp2.append(f2.val)
            f2 = f2.next
        # 1.2合并两个List后进行排序。
        temp = temp1 + temp2
        temp.sort()
        # 1.3设置dummy，并且用List里面的值逐个填充新链表ff。
        dummy = ff = ListNode(0)
        for i in temp:
            ff.next = ListNode(i)
            ff = ff.next
        return dummy.next
# s = Solution()
# re = s.mergeTwoLists()
s = "fsdf"
r = s.lstrip('fd')
x = s.rstrip('fd')
print(x)
print(r)
q = s.split('s')
print(q)
w = s.join('jjs')
print(w)
e = s.partition('s')
print(e)
print(s[-1::-1])


def reverse(x: int) -> int:
    str_int = str(x)
    if str_int.startswith('-'):
        # print(str_int)
        str_int = str_int.lstrip('-')
        str1 = str_int[-1::-1]
        # print(str1)
        result = -int(str1)
        # print(str1)
    else:
        str1 = str_int[-1::-1]
        result = int(str1)
    if result not in range((-2)**31,(2**31)- 1):
        return 0

    return result

print(reverse(12301233333333333333333333333333333333333))
x = 'fff'
for i in x:
    print(i)