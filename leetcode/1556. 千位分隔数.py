class Solution:
    def thousandSeparator(self, n: int) -> str:
        s, ans = str(n), ''
        n = len(s)
        for i in range(n):
            if i > 0 and (n - i) % 3 == 0:
                ans += '.'
            ans += s[i]
        return ans


class Solution1:
    def thousandSeparator(self, n: int) -> str:
        # return format(n, ',').replace(',', '.')
        return '{:,}'.format(n).replace(',', '.')


ret = Solution1()
print(ret.thousandSeparator(9871233))
