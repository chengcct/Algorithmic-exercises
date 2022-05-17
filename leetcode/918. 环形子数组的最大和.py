# -*- coding:utf-8 -*-
# @Author : Cheng
# @Time : 2022/5/10 17:47
from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        max_ = float('-inf')
        # 无环
        pre = 0
        for i in range(n):
            pre = max(0, pre) + nums[i]
            max_ = max(max_, pre)
        # 如果最子数组和小于0，说明数组中全为负数，返回最大负数即可
        if max_ < 0:
            return max_
        # 有环
        pre = 0
        min_ = float('inf')
        for i in range(n):
            pre = min(0, pre) + nums[i]
            min_ = min(min_, pre)

        return max(max_, sum(nums) - min_)


if __name__ == '__main__':
    s = Solution()
    print(s.maxSubarraySumCircular([1, -2, 3, -2]))