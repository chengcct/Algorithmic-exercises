class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len1 = len(haystack)
        len2 = len(needle)
        for i in range(len1 - len2 + 1):
            while haystack[i:i + len2] == needle:
                return i
        return -1


ret = Solution()
print(ret.strStr('hello', 'll'))
