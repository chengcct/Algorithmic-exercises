# -*- coding:utf-8 -*-
# @Author : Cheng
# @Time : 2022/1/10 15:36
class Solution:
    @staticmethod
    def isAdditiveNumber(num: str) -> bool:
        def check(x, y):
            a = int(num[:x + 1])
            b = int(num[x + 1:y + 1])
            if (x > 0 and num[0] == '0') or ((y > x + 1) and num[x + 1] == '0'):
                # 数字多于一位但有前导0的情况
                return False
            while True:
                if y == n - 1:  # b的最后一位是 num[n-1]，迭代结束
                    return True
                c = a + b  # 期望的 a+b = c 值
                cstr = str(c)  # c的string表示
                k = y + len(cstr)  # 正确情况下 k的坐标值
                if k > n:
                    return False
                if num[y + 1:k + 1] != cstr:  # 判断 实际字符串 和 期望值(cstr) 是否相等
                    return False
                else:
                    x, y = y, k
                    a, b = b, c

        n = len(num)
        for x in range(n - 2):
            for y in range(x + 1, n - 1):
                if check(x, y):
                    return True
        return False


if __name__ == '__main__':
    Solution.isAdditiveNumber("112358")
