class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n in [3 ** i for i in range(0, 21)]


class Solution1:
    def isPowerOfThree(self, n: int) -> bool:
        while n >= 3:
            n /= 3
        return True if n == 1 else False


ret = Solution()
print(ret.isPowerOfThree(27))
