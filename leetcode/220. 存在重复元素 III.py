from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        bucker = {}
        for i in range(len(nums)):
            # 计算分桶索引，桶宽t+1， 左闭右开
            pos = nums[i] // (t + 1)
            # 两元素在一个桶内
            if pos in bucker:
                return True
            # 两元素在相邻桶内，且相差小于t
            if pos - 1 in bucker and abs(nums[i] - bucker[pos - 1]) <= t:
                return True
            if pos + 1 in bucker and abs(nums[i] - bucker[pos + 1]) <= t:
                return True
            bucker[pos] = nums[i]
            # 若当前元素索引大于k，删除索引为i-k的元素所在桶
            if i >= k:
                del bucker[nums[i - k] // (t + 1)]
        return False


ret = Solution()
print(ret.containsNearbyAlmostDuplicate([1, 2, 3, 1], 3, 0))
