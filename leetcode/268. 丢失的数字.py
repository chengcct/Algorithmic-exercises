from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return len(nums) * (len(nums) + 1) // 2 - sum(nums)


ret = Solution()
print(ret.missingNumber([3, 0, 1]))
