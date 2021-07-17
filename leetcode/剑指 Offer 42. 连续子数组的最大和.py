from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        db = nums[0]
        max_sum = db
        for i in range(1, len(nums)):
            db = max(nums[i], nums[i]+db)
            max_sum = max(max_sum, db)
        return max_sum