class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        """
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """
        maxLen = left = diffs = 0
        for right in range(len(s)):
            diffs += abs(ord(s[right]) - ord(t[right]))
            while diffs > maxCost and left <= right:
                diffs -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            maxLen = max(right - left + 1, maxLen)
        return maxLen


sol = Solution()
print(sol.equalSubstring("abcd", "cdef", 1))
