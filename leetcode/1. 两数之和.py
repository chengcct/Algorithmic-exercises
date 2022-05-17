# -*- coding:utf-8 -*-
# @Author : Cheng
# @Time : 2022/4/25 17:38
from collections import defaultdict
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = defaultdict()
        for i, num in enumerate(nums):
            if num in cache:
                return [cache.get(num), i]
            cache[target - num] = i


if __name__ == '__main__':
    nums = [12, 11, 2, 11, 15, 7]
    target = 9
    s = Solution1()
    print(s.twoSum(nums, target))
