class Solution:
    def reverseBits(self, n: int) -> int:
        """
        python对于输入的二进制数直接转为十进制
        所以n已经是十进制数了，再用bin转为二进制的时候前面的无效0会省去，也就是说可能不足32位，此时要用zfill函数，右对齐，前面的空位填充为0
        最后用切片[::-1]
        倒置，求十进制即可
        """
        return int(bin(n)[2::].zfill(32)[::-1], base=2)


ret = Solution()
print(ret.reverseBits(0o0000010100101000001111010011100))

