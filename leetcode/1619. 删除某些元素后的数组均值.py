from typing import List


class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        n = int(len(arr) * 0.05)
        return 1.0 * sum(arr[n:n * (-1)]) / (len(arr) - 2 * n)


ret = Solution()
print(ret.trimMean([1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3]))
