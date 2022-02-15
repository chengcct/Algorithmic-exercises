# -*- coding:utf-8 -*-
# @Author : Cheng
# @Time : 2022/1/19 10:33
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        bag = set()
        for i, j in enumerate(nums):
            if len(bag) == k + 1:
                bag.remove(nums[i - 1 - k])
            if j in bag:
                return True
            bag.add(j)
        return False


if __name__ == '__main__':
    print(Solution().containsNearbyDuplicate([1, 2, 3, 1], 3))
