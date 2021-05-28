class Solution:
    def findNthDigit(self, n: int) -> int:
        base = 9
        cur_sum, pre_sum = base, 0
        for i in range(1, 100000):
            if n <= cur_sum:
                # divmod返回商和余数
                div, mod = divmod(n - pre_sum - 1, i)
                num = 10 ** (i - 1) + div
                return int(str(num)[mod])
            base = (10 ** i) * (i + 1) * 9
            pre_sum = cur_sum
            cur_sum += base


ret = Solution()
print(ret.findNthDigit(30))
