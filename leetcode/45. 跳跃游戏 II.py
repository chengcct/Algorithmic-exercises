from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        far = 0
        end = 0
        jumps = 0
        for i in range(len(nums) - 1):
            far = max(far, nums[i] + i)
            if end == i:
                jumps += 1
                end = far
        return jumps


if __name__ == '__main__':
    ret = Solution()
    print(ret.jump([2, 3, 1, 1, 4]))
