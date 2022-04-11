# -*- coding:utf-8 -*-
# @Author : Cheng
# @Time : 2022/4/11 17:24
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        res = 1
        product = 9
        for i in range(1, n + 1):
            res += product
            product *= (10 - i)
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.countNumbersWithUniqueDigits(2))