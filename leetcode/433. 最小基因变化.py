# -*- coding:utf-8 -*-
# @Author : Cheng
# @Time : 2022/5/7 17:04
from collections import deque
from typing import List


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if start == end:
            return 0
        bank = set(bank)
        if end not in bank:
            return -1
        q = deque([(start, 0)])
        while q:
            cur, step = q.popleft()
            for nxt in list(bank):
                count = 0
                for i in range(len(cur)):
                    if cur[i] != nxt[i]:
                        count += 1
                # 只有一个字符不同，nxt 是由cur变换过来的
                if count == 1:
                    if nxt == end:
                        return step + 1
                    bank.remove(nxt)
                    q.append((nxt, step + 1))
        return -1


if __name__ == '__main__':
    s = Solution()
    start = "AACCGGTT"
    end = "AACCGGTA"
    bank = ["AACCGGTA"]
    print(s.minMutation(start, end, bank))