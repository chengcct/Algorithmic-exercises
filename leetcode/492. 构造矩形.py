import math


class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        if area == 1:
            return [1, 1]
        for i in range(int(math.sqrt(area)), area + 1):
            if area % i == 0:
                return [i, area // i] if i >= area // i else [area // i, i]


class Solution1(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        a = int(area ** 0.5)
        for i in range(a, 0, -1):
            j = area / i
            while j % 1 == 0:
                return int(j), i


ret = Solution1()
print(ret.constructRectangle(6))
