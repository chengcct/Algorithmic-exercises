# -*- coding:utf-8 -*-
# @Author : Cheng
# @Time : 2022/5/16 17:13
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True
        for i in range(1, len(s) + 1):
            for word in wordDict:
                dp[i] = dp[i] or (dp[i - len(word)] and s[i - len(word):i] == word)
        return dp[-1]


if __name__ == '__main__':
    s = "applepenapple"
    wordDict = ["apple", "pen"]
    solution = Solution()
    print(solution.wordBreak(s, wordDict))
