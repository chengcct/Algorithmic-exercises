# -*- coding:utf-8 -*-
# @Author : Cheng
# @Time : 2022/1/11 15:35
from collections import defaultdict
from typing import List


class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        ban, n, DIR = defaultdict(set), len(blocked), ((0, 1), (0, -1), (1, 0), (-1, 0))
        for x, y in blocked:
            ban[x].add(y)

        def check(i, j):
            seen, q = defaultdict(set), [i]
            while q:
                x, y = q.pop()
                for dx, dy in DIR:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < 1000000 and 0 <= ny < 1000000 and ny not in ban[nx] and ny not in seen[nx]:
                        if [nx, ny] == j: return True
                        if abs(nx - i[0]) + abs(ny - i[1]) > n:
                            return True
                        q.append([nx, ny])
                        seen[nx].add(ny)
            return False

        return check(source, target) and check(target, source)


if __name__ == '__main__':
    Solution().isEscapePossible(blocked=[], source=[0, 0], target=[999999, 999999])
