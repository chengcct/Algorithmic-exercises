def checkPossibility(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    count = 0
    for i in range(len(nums) - 1):
        while nums[i] > nums[i + 1]:
            count += 1
            while count > 1:
                return False
            if i == 0:
                nums[i] = nums[i + 1]
            else:
                if nums[i - 1] <= nums[i + 1]:
                    nums[i] = nums[i + 1]
                else:
                    nums[i + 1] = nums[i]
    return True


class Solution(object):
    pass


ret = Solution()
print(checkPossibility([4, 5, 1, 0]))
# print(ret.checkPossibility([4, 2, 3]))
