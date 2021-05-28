from typing import List


class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        res = A[0]
        ans = 0
        for i in range(1, len(A)):
            res -= 1
            ans = max(ans, A[i] + res)
            res = max(res, A[i])
        return ans


ret = Solution()
print(ret.maxScoreSightseeingPair([8, 1, 5, 2, 6]))
