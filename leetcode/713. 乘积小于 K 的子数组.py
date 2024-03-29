# -*- coding:utf-8 -*-
# @Author : Cheng
# @Time : 2022/5/5 17:27
from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        ans = 0
        prod = 1
        left = 0
        for right, val in enumerate(nums):
            prod *= val
            while prod >= k:
                prod /= nums[left]
                left += 1
            ans += right - left + 1
        return ans


if __name__ == '__main__':
    s = Solution()
    nums = [10, 5, 2, 6]
    k = 100
    print(s.numSubarrayProductLessThanK(nums, k))
