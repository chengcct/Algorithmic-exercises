# -*- coding:utf-8 -*-
# @Author : Cheng
# @Time : 2022/4/1 16:50
import collections
from typing import List


class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        cnt = collections.Counter(arr)
        if cnt[0] % 2:
            return False
        for x in sorted(cnt, key=abs):
            if cnt[x] > cnt[2 * x]:
                return False
            cnt[2 * x] -= cnt[x]
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.canReorderDoubled([4,-2,2,-4]))
