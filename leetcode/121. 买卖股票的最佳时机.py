from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        max_f = 0
        pre_f = 0
        for i in range(1, len(prices)):
            pre_f = max(pre_f, 0) + prices[i] - prices[i - 1]
            max_f = max(max_f, pre_f)
        return max_f


ret = Solution()
print(ret.maxProfit([7, 1, 5, 3, 6, 4]))
