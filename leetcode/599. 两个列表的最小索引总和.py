# -*- coding:utf-8 -*-
# @Author : Cheng
# @Time : 2022/3/14 17:27
from collections import defaultdict
from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        res = defaultdict(list)
        for i in set(list1) & set(list2):
            res[list1.index(i) + list2.index(i)].append(i)
        return min(res.items())[1]


if __name__ == '__main__':
    a = Solution()
    r = a.findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC", 'asdasd'],
                     ["KFC", "The Grill at Torrey Pines", 'asdasd', "Hungry Hunter Steakhouse", "Shogun"])
    print(r)