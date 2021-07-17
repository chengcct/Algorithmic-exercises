from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res, n = [], len(nums)
        for num in nums:
            k = abs(num)
            # 说明k之前出现过 它重复了！
            if nums[k - 1] < 0:
                res.append(k)
            else:
                nums[k - 1] = -nums[k - 1]
        for x in range(1, n + 1):
            # 说明k没有出现过
            if nums[x - 1] > 0:
                res.append(x)
        return res


if __name__ == '__main__':
    ret = Solution()
    print(ret.findErrorNums([1, 2, 2, 4]))
