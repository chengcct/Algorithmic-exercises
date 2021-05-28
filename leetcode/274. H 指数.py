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


ret = Solution()
print(ret.hIndex([3, 0, 6, 1, 5]))
