# -*- coding:utf-8 -*-
# @Author : Cheng
# @Time : 2022/5/12 16:04
from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        return sum(list(col) != sorted(col) for col in zip(*strs))


if __name__ == '__main__':
    s = Solution()
    print(s.minDeletionSize(["zyx", "wvu", "tsr"]))
