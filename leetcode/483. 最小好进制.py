class Solution:
    def smallestGoodBase(self, n: str) -> str:
        num = int(n)
        # n = x^(m-1) + x^(m-2) + ... + x + 1
        for m in range(num.bit_length(), 2, -1):
            # 二项式展开 x^(m-1) < n < (x+1)^(m-1)
            x = int(pow(num, 1 / (m - 1)))
            # 等比数列求和 n = (x^m - 1)/(x-1)
            if num == (pow(x, m) - 1) // (x - 1):
                return str(x)
        return str(num - 1)


if __name__ == '__main__':
    s = Solution()
    print(s.smallestGoodBase('13'))
