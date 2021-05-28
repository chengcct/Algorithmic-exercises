class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # ^是异或
        return bin(x ^ y).count('1')


ret = Solution()
print(ret.hammingDistance(1, 4))
