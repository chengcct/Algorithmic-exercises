from typing import List
import collections


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        # 辗转相除法
        def gcd(nun1, num2):
            while nun1 % num2 != 0:
                nun1, num2 = num2, nun1 % num2
            return num2

        Hash = collections.Counter(deck)
        count = list(Hash.values())
        for i in range(len(count) - 1):
            count[i + 1] = gcd(count[i], count[i + 1])

        return count[-1] > 1


ret = Solution()
print(ret.hasGroupsSizeX([1, 2, 3, 4, 4, 3, 2, 1]))
