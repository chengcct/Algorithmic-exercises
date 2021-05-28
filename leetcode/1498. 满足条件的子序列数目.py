import bisect
from typing import List


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        for i, j in enumerate(nums):
            if target // 2 >= j:
                # <<:左移运算符
                # z = bisect.bisect_right(nums, target - j)
                res += 1 << (bisect.bisect_right(nums, target - j) - 1 - i)
        return res % (10 ** 9 + 7)


ret = Solution()
print(ret.numSubseq([3, 5, 6, 7], 9))
