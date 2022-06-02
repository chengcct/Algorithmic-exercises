# -*- coding:utf-8 -*-
# @Author : Cheng
# @Time : 2022/5/25 17:34
from itertools import pairwise


class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        dp, cur = [0] * 26, 1
        dp[ord(p[0]) - ord('a')] = 1
        for c1, c2 in pairwise(p):
            if not (ord(c2) - ord(c1) - 1) % 26:
                cur += 1
            else:
                cur = 1
            dp[idx] = max(dp[idx := ord(c2) - ord('a')], cur)
        return sum(dp)


if __name__ == '__main__':
    s = Solution()
    print(s.findSubstringInWraproundString("zab"))
