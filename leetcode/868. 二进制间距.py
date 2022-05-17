# -*- coding:utf-8 -*-
# @Author : Cheng
# @Time : 2022/4/24 16:51
class Solution:
    def binaryGap(self, n: int) -> int:
        num = bin(n)[2:]
        idx = 0
        is_cur = False
        max_len = 0
        for i, j in enumerate(num):
            if j == '1' and is_cur == False:
                idx = i
                is_cur = True
            elif j == '1' and is_cur == True:
                max_len = max(max_len, i - idx)
                idx = i
        return max_len


if __name__ == '__main__':
    s = Solution()
    print(s.binaryGap(13))
