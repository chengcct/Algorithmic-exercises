# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2  # l1如果没有了，那就调用l2
        if not l2:
            return l1  # l2如果没有了, 那就调用l2
        if l1.val <= l2.val:  # 将较小的结点 append 到当前的链表中
            l1.next = self.mergeTwoLists(l1.next, l2)  # l1走一步，l2不走
            return l1  # 返回l1
        else:  # l2较小，结果链表中应该 append l2
            l2.next = self.mergeTwoLists(l1, l2.next)  # l2走一步, l1不走
            return l2  # 返回l2

# l1 = [1,2,4], l2 = [1,3,4]
