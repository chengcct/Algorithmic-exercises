# -*- coding:utf-8 -*-
# @Author : Cheng
# @Time : 2022/5/7 17:24
from typing import List

import collections


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # 创建 nums中的值出现的次数 mapping. Key 为 nums[i], value 为 nums[i] 出现的次数
        numsMap = collections.Counter(nums)

        # nums 的最大的数字
        maxLen = max(numsMap.keys())
        # dp 数组从 1 开始计算, 0 空出来
        dp = [0] * (maxLen + 1)

        # 1 出现的次数之和
        dp[1] = 1 * numsMap[1]

        for i in range(2, maxLen + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + i * numsMap[i])
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.deleteAndEarn([3, 4, 2]))
    print(s.deleteAndEarn([2, 2, 3, 3, 3, 4]))
