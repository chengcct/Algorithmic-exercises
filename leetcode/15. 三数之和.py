from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []
        # 枚举第一个元素
        for i in range(n - 2):
            # 如果最小数大于0，不存在解
            if nums[i] > 0:
                break
            # 确保first不重复
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            second, third = i + 1, n - 1
            while second < third:
                target = 0 - nums[i]
                s = nums[second] + nums[third]
                # 右指针左移
                if s > target:
                    third -= 1
                # 左指针右移
                elif s < target:
                    second += 1
                # 左指针右移且右指针左移
                else:
                    ans.append([nums[i], nums[second], nums[third]])
                    second += 1
                    third -= 1
                    while third > second and nums[third] == nums[third + 1]:
                        third -= 1
                    while third > second and nums[second] == nums[second - 1]:
                        second += 1
        return ans


ret = Solution()
print(ret.threeSum([-1, 0, 1, 2, -1, -4]))
