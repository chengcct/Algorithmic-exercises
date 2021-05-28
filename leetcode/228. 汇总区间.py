from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        i, n = 0, len(nums)
        while i < n:
            if i + 1 < n and nums[i + 1] == nums[i] + 1:
                j = i
                while i + 1 < n and nums[i + 1] == nums[i] + 1:
                    i += 1
                res.append(str(nums[j]) + '->' + str(nums[i]))
            else:
                res.append(str(nums[i]))
            i += 1
        return res


ret = Solution()
print(ret.summaryRanges([0, 1, 2, 4, 5, 7]))
