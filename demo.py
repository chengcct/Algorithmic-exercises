class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


head = None

for i in range(1, 6):
    head = Node(i, head)

while head is not None:
    print(head.data)
    head = head.next
