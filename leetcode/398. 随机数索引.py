# -*- coding:utf-8 -*-
# @Author : Cheng
# @Time : 2022/4/25 17:18
import random
from collections import defaultdict
from typing import List


class Solution:
    def __init__(self, nums: List[int]):
        self.nums_dicts = defaultdict(list)
        for i, num in enumerate(nums):
            self.nums_dicts[num].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.nums_dicts[target])


if __name__ == '__main__':
    nums = [1, 2, 3, 3, 3]
    solution = Solution(nums)
    print(solution.pick(3))
