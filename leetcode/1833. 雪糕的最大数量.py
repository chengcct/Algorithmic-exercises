from typing import List


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        list1 = sorted(costs)
        x, sum = 0, 0
        for j in list1:
            if x + j <= coins:
                x += j
                sum += 1
        return sum


if __name__ == '__main__':
    s = Solution()
    # print(s.maxIceCream([7, 3, 3, 6, 6, 6, 10, 5, 9, 2], 56))
    # print(s.maxIceCream([1, 3, 2, 4, 1], 7))
    print(s.maxIceCream(
        [2, 34, 17, 42, 100, 2, 36, 2, 82, 66, 27, 82, 38, 54, 14, 82, 52, 34, 44, 3, 36, 8, 27, 54, 18, 74, 51, 32, 32,
         27, 2, 30, 92, 46, 34, 92, 54, 2, 22, 24, 78, 72, 52, 50, 34, 2, 49, 86, 18, 80, 87, 66, 7, 24, 90, 52, 82, 16,
         30, 94, 62, 56, 30, 32, 8, 40, 49, 12, 62, 34, 80, 42, 73, 2, 94, 3, 56, 16, 18, 52, 6, 37, 14, 33, 96, 47, 62,
         98, 7, 55, 57, 48, 99, 96, 97, 36, 37, 98, 2, 98], 67))
