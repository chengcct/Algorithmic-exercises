# -*- coding:utf-8 -*-
# @Author : Cheng
# @Time : 2022/4/22 17:35
from typing import List


class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        init_sum = sum(i * nums[i] for i in range(n))
        total = sum(nums)
        pre = init_sum
        ans = init_sum
        for i in range(1, n):
            cur = pre + total - n * nums[n - i]
            ans = max(ans, cur)
            pre = cur
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.maxRotateFunction([4, 3, 2, 6]))
