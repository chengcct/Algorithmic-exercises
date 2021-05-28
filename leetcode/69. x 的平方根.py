class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x + 1
        while left < right:
            mid = left + (right - left) // 2
            if mid ** 2 == x:
                return mid
            elif mid ** 2 < x:
                left = mid + 1
            else:
                right = mid
        return left - 1


ret = Solution()
print(ret.mySqrt(8))
