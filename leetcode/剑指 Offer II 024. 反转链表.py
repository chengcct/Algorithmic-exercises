# -*- coding:utf-8 -*-
# @Author : Cheng
# @Time : 2022/4/24 17:44
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre, cur = None, head
        while cur:
            cur.next, pre, cur = pre, cur, cur.next
        return pre


if __name__ == '__main__':
    listnode = None
    for i in range(1, 6):
        listnode = ListNode(i, listnode)
    s = Solution()
    print(s.reverseList(listnode))
