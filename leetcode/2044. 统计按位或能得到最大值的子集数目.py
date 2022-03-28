# -*- coding:utf-8 -*-
# @Author : Cheng
# @Time : 2022/3/15 16:19
import collections
from typing import List


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        dp = collections.Counter([0])
        for i in nums:
            for k, v in dp.copy().items():
                dp[k | i] += v
        return dp[max(dp)]


if __name__ == '__main__':
    s = Solution()
    res = s.countMaxOrSubsets([3, 1])
    print(res)