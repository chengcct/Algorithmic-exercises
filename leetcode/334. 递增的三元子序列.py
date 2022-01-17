# -*- coding:utf-8 -*-
# @Author : Cheng
# @Time : 2022/1/12 10:08
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        l = len(nums)
        if l < 3 or len(set(nums)) < 3:
            return False
        first, second = nums[0], float('inf')
        for i in range(1, l):
            num = nums[i]
            if num > second:
                return True
            if num > first:
                second = num
            else:
                first = num
        return False


if __name__ == '__main__':
    print(Solution().increasingTriplet([13, 12, 34, 4, 5]))
