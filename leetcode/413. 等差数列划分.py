# -*- coding:utf-8 -*-
# @Author : Cheng
# @Time : 2022/5/16 17:39
from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        l = len(nums)
        res = 0
        if l < 3:
            return res
        pre = 0
        for i in range(2, l):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                tmp = pre + 1
                pre = tmp
                res += tmp
            else:
                pre = 0
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.numberOfArithmeticSlices([1, 2, 3, 4]))
