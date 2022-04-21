# -*- coding:utf-8 -*-
# @Author : Cheng
# @Time : 2022/4/12 17:45
from typing import List


class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        line = 1
        width = 0
        for i in s:
            width += widths[ord(i) - ord('a')]
            if width > 100:
                line += 1
                width = widths[ord(i) - ord('a')]
        return [line, width]


if __name__ == '__main__':
    s = Solution()
    print(s.numberOfLines(
        [4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
        "bbbcccdddaaa"))
