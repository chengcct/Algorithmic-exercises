from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_max(nums):
            length = len(nums)
            if not nums:
                return 0
            if length == 1:
                return nums[0]

            res = [0] * length
            res[0] = nums[0]
            res[1] = max(nums[0], nums[1])

            for i in range(2, length):
                res[i] = max(res[i - 1], res[i - 2] + nums[i])
            return res[length - 1]

        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        """
        我们可以把题目分成两个部分
        在 [0:n-1] 中找到最大值
        在 [1:n] 中找到最大值
        """
        nums1 = nums[1:]
        nums2 = nums[0:len(nums) - 1]
        return max(rob_max(nums1), rob_max(nums2))


if __name__ == '__main__':
    print(Solution().rob([1, 3, 1, 3, 100]))
