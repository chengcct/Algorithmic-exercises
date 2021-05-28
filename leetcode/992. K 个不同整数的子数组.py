from typing import List
from collections import Counter


class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        def atMost(A, K):
            count = Counter()
            res = i = 0
            for j, num in enumerate(A):
                if count[num] == 0:
                    K -= 1
                count[num] += 1
                while K < 0:
                    count[A[i]] -= 1
                    if count[A[i]] == 0:
                        K += 1
                    i += 1
                res += j - i + 1
            return res

        return atMost(A, K) - atMost(A, K - 1)


# 滑动窗口
class Solution1:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        # n = len(A)
        num1, num2 = Counter(), Counter()
        tot1 = tot2 = 0
        left1 = left2 = 0
        res = 0

        for right, num in enumerate(A):
            if num1[num] == 0:
                tot1 += 1
            num1[num] += 1
            if num2[num] == 0:
                tot2 += 1
            num2[num] += 1

            while tot1 > K:
                num1[A[left1]] -= 1
                if num1[A[left1]] == 0:
                    tot1 -= 1
                left1 += 1
            while tot2 > K - 1:
                num2[A[left2]] -= 1
                if num2[A[left2]] == 0:
                    tot2 -= 1
                left2 += 1

            res += left2 - left1

        return res


ret = Solution1()
print(ret.subarraysWithKDistinct([1, 2, 1, 2, 3], 2))
