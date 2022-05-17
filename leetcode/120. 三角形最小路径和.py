# -*- coding:utf-8 -*-
# @Author : Cheng
# @Time : 2022/5/17 17:41
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        dp = triangle[-1]
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]
        return dp[0]


if __name__ == '__main__':
    triangle = [[-1], [2, 3], [1, -1, -3]]
    print(Solution().minimumTotal(triangle))
