# -*- coding:utf-8 -*-
# @Author : Cheng
# @Time : 2022/3/31 17:30
from copy import deepcopy
from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        sortedArr = deepcopy(arr)
        for i in range(1, len(arr)):
            sortedArr[i] = arr[i] - arr[i - 1]
        sortedArr[0] = min(sortedArr[1:])
        ans = []
        for j in range(1, len(arr)):
            if sortedArr[j] == sortedArr[0]: ans.append([arr[j - 1], arr[j]])
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.minimumAbsDifference([3, 8, -10, 23, 19, -4, -14, 27]))

"""
输入：arr = [4,2,1,3]
输出：[[1,2],[2,3],[3,4]]
"""
