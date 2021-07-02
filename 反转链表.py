class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def nonrecurse(self, head):
        if head is None or head.next is None:
            return head
        pre, cur, h = None, head, head
        while cur:
            h = cur
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return h

    def recure(self, head, newhead):
        if head is None:
            return
        if head.next is None:
            newhead = head
        else:
            newhead = self.recure(head.next, newhead)
            head.next.next = head
            head.next = None
        return newhead
