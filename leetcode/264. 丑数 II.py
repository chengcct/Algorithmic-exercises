# -*- coding:utf-8 -*-
# @Author : Cheng
# @Time : 2022/5/17 17:30
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        i2, i3, i5 = 0, 0, 0
        res = [1]
        while len(res) < n:
            m2, m3, m5 = res[i2] * 2, res[i3] * 3, res[i5] * 5
            m = min(m2, m3, m5)
            if m == m2:
                i2 += 1
            if m == m3:
                i3 += 1
            if m == m5:
                i5 += 1
            res.append(m)
        return res[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.nthUglyNumber(10))