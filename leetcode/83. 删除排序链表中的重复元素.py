# Definition for singly-linked list.
"""
输入：head = [1,1,2]
输出：[1,2]
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        while head and head.next:
            if head.val == head.next.val:  # 前后两个值相等, 当前节点指向当前节点的下下一个节点, 先不走
                head.next = head.next.next
            else:  # 前后两个值不等, 当前节点向后走一步
                head = head.next
        return cur



