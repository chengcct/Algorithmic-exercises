from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        ans = 0
        tmp = []
        for x, y in costs:
            ans += y
            tmp.append(x - y)
        tmp.sort()
        for i in tmp[:len(tmp) // 2]:
            ans += i
        return ans


ret = Solution()
print(ret.twoCitySchedCost([[10, 20], [30, 200], [400, 50], [30, 20]]))
