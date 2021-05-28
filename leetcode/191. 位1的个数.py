class Solution:
    def hammingWeight(self, n: int) -> int:
        return str(bin(n)).count('1')


ret = Solution()
print(ret.hammingWeight(0o0000000000000000000000000001011))