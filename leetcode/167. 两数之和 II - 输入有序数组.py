from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            if target - numbers[j] == numbers[i]:
                return [i + 1, j + 1]
            elif numbers[j] + numbers[i] > target:
                j -= 1
            else:
                i += 1
        return []


ret = Solution()
print(ret.twoSum([2, 7, 11, 15], 9))
