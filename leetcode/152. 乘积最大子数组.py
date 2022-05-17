# -*- coding:utf-8 -*-
# @Author : Cheng
# @Time : 2022/5/10 17:53
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return nums[0]
        dp_max = [0] * n
        dp_max[0] = nums[0]

        dp_min = [0] * n
        dp_min[0] = nums[0]
        ret = nums[0]
        for i in range(1, n):
            dp_max[i] = max(nums[i], dp_max[i - 1] * nums[i], dp_min[i - 1] * nums[i])
            dp_min[i] = min(nums[i], dp_max[i - 1] * nums[i], dp_min[i - 1] * nums[i])
            ret = max(ret, dp_max[i])
        return ret


if __name__ == '__main__':
    s = Solution()
    print(s.maxProduct([2, 3, -2, 4]))
