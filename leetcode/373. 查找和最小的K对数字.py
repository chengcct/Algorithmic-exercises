# -*- coding:utf-8 -*-
# @Author : Cheng
# @Time : 2022/1/14 10:37
import heapq
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        l1, l2 = len(nums1), len(nums2)
        res, minHeap = [], []
        heapq.heapify(minHeap)
        for i in range(min(k, l1)):
            heapq.heappush(minHeap, (nums1[i] + nums2[0], i, 0))

        cnt = 0
        while minHeap and cnt < k:
            _, i, j = heapq.heappop(minHeap)
            cnt += 1
            res.append([nums1[i], nums2[j]])
            if j + 1 < l2:
                heapq.heappush(minHeap, (nums1[i] + nums2[j + 1], i, j + 1))
        return res


if __name__ == '__main__':
    s = Solution().kSmallestPairs([1, 7, 11], [2, 4, 6], 3)
    print(s)
