from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:m + n] = nums2[:n]
        return nums1.sort()


ret = Solution()
print(ret.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
