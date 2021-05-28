# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head:
            self.count = 0
            return head
        head.next = self.removeNthFromEnd(head.next, n)  # 递归调用
        self.count += 1  # 回溯时进行节点计数
        return head.next if self.count == n else head


ret = Solution()
print(ret.removeNthFromEnd([1, 2, 3, 4, 5], 2))
