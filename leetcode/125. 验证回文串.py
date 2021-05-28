class Solution:
    def isPalindrome(self, s: str) -> bool:
        # a = filter(str.isalnum, s.lower())
        # # print(a)
        s = ''.join(filter(str.isalnum, s.lower()))
        # print(s)
        return s == s[::-1]

ret = Solution()
print(ret.isPalindrome("race a car"))