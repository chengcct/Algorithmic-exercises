# -*- coding:utf-8 -*-
# @Author : Cheng
# @Time : 2022/3/31 17:24
from typing import List


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        l = len(pref)
        count = 0
        for i in words:
            if i[:l] == pref:
                count += 1
        return count


if __name__ == '__main__':
    s = Solution()
    print(s.prefixCount(["pay", "attention", "practice", "attend"], "at"))

