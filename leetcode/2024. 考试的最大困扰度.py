# -*- coding:utf-8 -*-
# @Author : Cheng
# @Time : 2022/3/29 17:11
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        no = []
        yes = []
        n = len(answerKey)

        for i in range(n):
            if answerKey[i] == 'F':
                no.append(i + 1)
            else:
                yes.append(i + 1)

        m1 = len(no)
        m2 = len(yes)
        if k >= m1:
            return n
        if k >= m2:
            return n

        no.append(0)
        no.append(n + 1)

        yes.append(0)
        yes.append(n + 1)

        m1 = len(no)
        m2 = len(yes)

        res = 0

        no.sort()
        yes.sort()

        # m 中选取 k个 的最大情况
        for i in range(1, m1 - k):
            left = no[i - 1]
            right = no[i + k] - 1
            # print(left, right)
            res = max(res, right - left)

        for i in range(1, m2 - k):
            left2 = yes[i - 1]
            right2 = yes[i + k] - 1
            res = max(res, right2 - left2)

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.maxConsecutiveAnswers('TTFF', 1))
