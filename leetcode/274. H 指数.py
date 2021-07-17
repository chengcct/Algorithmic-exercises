from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if citations == [] or max(citations) == 0:
            return 0
        s = sorted(citations)
        n = len(s)
        for i in range(n):
            if s[i] >= (n - i):
                return n - i


class Solution1:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        for i in range(len(citations)):
            if citations[i] < i + 1:
                return i
        else:
            return len(citations)


ret = Solution1()
print(ret.hIndex([3, 0, 6, 1, 5]))
