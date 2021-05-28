from typing import List


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        # 如果比较符号在子数组中的每个相邻元素对之间翻转，则该子数组是湍流子数组。
        N = len(arr)
        up = [1] * N
        down = [1] * N
        res = 1
        for i in range(1, N):
            if arr[i - 1] < arr[i]:
                up[i] = down[i - 1] + 1
            elif arr[i - 1] > arr[i]:
                down[i] = up[i - 1] + 1
            res = max(res, max(up[i], down[i]))
        return res


ret = Solution()
# print(ret.maxTurbulenceSize([9, 4, 2, 10, 7, 8, 8, 1, 9]))
print(ret.maxTurbulenceSize([4, 8, 12, 16]))
