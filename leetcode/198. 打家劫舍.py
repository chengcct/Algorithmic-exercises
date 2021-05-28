from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if not nums:
            return 0
        while n == 1:
            return nums[0]
        while n == 2:
            return max(nums)
        dp1, dp2 = nums[0], max(nums[:2])
        for i in range(2, n):
            dp1, dp2 = dp2, max(dp2, dp1 + nums[i])
        return dp2


ret = Solution()
# print(ret.rob([1, 2, 3, 1]))
print(ret.rob([2, 7, 9, 3, 1]))
