# -*- coding:utf-8 -*-
# @Author : Cheng
# @Time : 2022/3/31 17:12
from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        alist = []
        for i in range(left, right + 1):
            if self.isSelfDividing(i):
                alist.append(i)
        return alist

    def isSelfDividing(self, num):
        if num < 10:
            return True
        else:
            for i in str(num):
                if int(i) == 0 or num % int(i) != 0:
                    return False
            return True


if __name__ == '__main__':
    s = Solution()
    s.selfDividingNumbers(1, 22)

"""
输入：left = 1, right = 22
输出：[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
"""
