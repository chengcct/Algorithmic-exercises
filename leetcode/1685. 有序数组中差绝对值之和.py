from typing import List


class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        tmp = []
        for i in range(1, len(nums)):
            tmp.append(nums[i] - nums[i - 1])
        r = sum(nums) - nums[0] * len(nums)
        res = [r]
        for i in range(len(tmp)):
            r += (2 * i - len(nums) + 2) * tmp[i]
            res.append(r)
        return res


ret = Solution()
# print(ret.getSumAbsoluteDifferences([2, 3, 5]))
print(ret.getSumAbsoluteDifferences([1, 4, 6, 8, 10]))
