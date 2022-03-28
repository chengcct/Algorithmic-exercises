# -*- coding:utf-8 -*-
# @Author : Cheng
# @Time : 2022/3/17 17:36
from typing import List


class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        max_word = ''
        a_set = set()
        for word in words:
            if len(word) == 1 or word[:-1] in a_set:
                a_set.add(word)
                if len(word) > len(max_word):
                    max_word = word
        return max_word


if __name__ == '__main__':
    s = Solution()
    print(s.longestWord(["a", "banana", "app", "appl", "ap", "apply", "apple"]))
