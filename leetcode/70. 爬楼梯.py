class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        a, b, tmp = 1, 2, 0
        for i in range(3, n + 1):
            tmp = a + b
            a = b
            b = tmp
        return tmp


if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(5))
