from heapq import heappush, heappop


class DinnerPlates:

    def __init__(self, capacity: int):
        self.stack = []
        self.heap = []
        self.capacity = capacity

    def push(self, val: int) -> None:
        if self.heap and self.heap[0] >= len(self.stack):
            self.heap = []
        if not self.heap:
            self.stack.append([val])
            if self.capacity > 1:
                heappush(self.heap, len(self.stack) - 1)
        else:
            idx = heappop(self.heap)
            self.stack[idx].append(val)
            if len(self.stack[idx]) < self.capacity:
                heappush(self.heap, idx)

    def pop(self) -> int:
        while self.stack and not self.stack[-1]:
            self.stack.pop()
        if not self.stack:
            return -1
        ans = self.stack[-1].pop()
        if not self.stack[-1]:
            self.stack.pop()
        return ans

    def popAtStack(self, index: int) -> int:
        if index >= len(self.stack) or not self.stack[index]:
            return -1
        if len(self.stack[index]) == self.capacity:
            heappush(self.heap, index)
        ans = self.stack[index].pop()
        return ans

# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)
