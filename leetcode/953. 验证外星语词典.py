# -*- coding:utf-8 -*-
# @Author : Cheng
# @Time : 2022/5/17 17:21
from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        return sorted(words, key=lambda x: [order.index(c) for c in x]) == words

if __name__ == '__main__':
    words = ["hello","leetcode"]
    order = "hlabcdefgijkmnopqrstuvwxyz"
    print(Solution().isAlienSorted(words, order))