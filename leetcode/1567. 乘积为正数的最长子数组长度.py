# -*- coding:utf-8 -*-
# @Author : Cheng
# @Time : 2022/5/10 17:57
from typing import List


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1 if nums[0] > 0 else 0
        pos = [0 for _ in range(n)]
        neg = [0 for _ in range(n)]
        ans = 0
        if nums[0] > 0:
            pos[0] = 1
            ans = 1
        elif nums[0] < 0:
            neg[0] = 1
        for i in range(1, n):
            if nums[i] > 0:
                pos[i] = pos[i - 1] + 1
                neg[i] = 0 if neg[i - 1] == 0 else neg[i - 1] + 1
            elif nums[i] < 0:
                neg[i] = pos[i - 1] + 1
                pos[i] = 0 if neg[i - 1] == 0 else neg[i - 1] + 1
            else:
                pos[i] = 0
                neg[i] = 0
            ans = max(ans, pos[i])
        return ans
