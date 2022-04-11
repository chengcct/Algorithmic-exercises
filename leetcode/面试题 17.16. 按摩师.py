# -*- coding:utf-8 -*-
# @Author : Cheng
# @Time : 2022/4/1 17:07
from typing import List


class Solution:
    def massage(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        for i in range(len(nums)):
            if i == 0:
                continue
            elif i == 1:
                nums[i] = max(nums[0:2])
            else:
                nums[i] = nums[i] + max(nums[0:i - 1])
        return max(nums)


if __name__ == '__main__':
    solution = Solution()
    print(solution.massage([1, 2, 3, 1]))
