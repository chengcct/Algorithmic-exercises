from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        for j, num in enumerate(nums):
            k += num
            if k < num * (j - i + 1):
                k -= nums[i]
                i += 1
        return j - i + 1


if __name__ == '__main__':
    res = Solution()
    print(res.maxFrequency([1, 2, 4], 5))
