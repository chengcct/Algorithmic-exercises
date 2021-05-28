import copy
import random
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.origin = copy.copy(nums)
        self.nums = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.origin

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        for i in range(len(self.nums) - 1, 0, -1):
            piovt = random.randint(0, i)
            self.nums[i], self.nums[piovt] = self.nums[piovt], self.nums[i]
        return self.nums

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
