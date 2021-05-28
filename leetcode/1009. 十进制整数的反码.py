class Solution:
    def bitwiseComplement(self, N: int) -> int:
        Nbin = bin(N)
        return 2 ** len(Nbin[2:]) - 1 - N


ret = Solution()
print(ret.bitwiseComplement(5))
