# -*- coding:utf-8 -*-
# @Author : Cheng
# @Time : 2022/3/25 16:53
class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n >= 5:
            count += n // 5
            n //= 5
        return count


if __name__ == '__main__':
    s = Solution()
    print(s.trailingZeroes(5))
