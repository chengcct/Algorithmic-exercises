class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # 比较反转后的后半部分与反转前的前半部分
        if s == '':
            return ''
        filp_s = s[::-1]
        for i in range(len(s)):
            length = len(s) - i
            while filp_s[i:] == s[:length]:
                return filp_s + s[length:]


ret = Solution()
print(ret.shortestPalindrome("abcd"))
