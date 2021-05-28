from typing import List


class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        maxlen = []
        for i in rectangles:
            maxlen.append(min(i))
        return maxlen.count(max(maxlen))


ret = Solution()
print(ret.countGoodRectangles([[5, 8], [3, 9], [5, 12], [16, 5]]))
