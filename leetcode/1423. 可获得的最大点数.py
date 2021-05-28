from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        ws = n - k
        s = sum(cardPoints[:ws])
        ms = s
        for i in range(ws, n):
            s += cardPoints[i] - cardPoints[i - ws]
            ms = min(ms, s)
        return sum(cardPoints) - ms


class Solution1:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        res = cursum = sum(cardPoints[-k:])
        for i in range(k):
            cursum += cardPoints[i] - cardPoints[-k+i]
            res = max(res, cursum)
        return res


ret = Solution1()
print(ret.maxScore([1, 2, 3, 4, 5, 6, 1], 3))
