from typing import List


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        res = [0] * num_people
        num = 1
        while candies > 0:
            idx = (num - 1) % num_people
            if candies >= num:
                res[idx] += num
                candies -= num
                num += 1
            else:
                res[idx] += candies
                candies = 0
        return res


ret = Solution()
print(ret.distributeCandies(7, 4))
