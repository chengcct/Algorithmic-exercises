from typing import List
import collections


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        for key, num in collections.Counter(arr).most_common(1):
            if num > len(arr) // 4:
                return key


ret = Solution()
print(ret.findSpecialInteger([1, 2, 2, 6, 6, 6, 6, 7, 10]))
