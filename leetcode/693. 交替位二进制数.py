# -*- coding:utf-8 -*-
# @Author : Cheng
# @Time : 2022/3/28 17:05
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        n1 = list(bin(n))
        for i, j in enumerate(n1[2:]):
            if j == n1[i + 1]:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.hasAlternatingBits(5))
