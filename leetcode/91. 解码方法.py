class Solution:
    def numDecodings(self, s: str) -> int:
        if s.startswith('0'):
            return 0
        n = len(s)
        dp = [1] * (n + 1)
        for i in range(2, n + 1):
            if s[i - 1] == '0' and s[i - 2] not in '12':
                return 0
            if s[i - 2:i] in ['10', '20']:
                dp[i] = dp[i - 2]
            elif '10' < s[i - 2:i] <= '26':
                dp[i] = dp[i - 1] + dp[i - 2]
            else:
                dp[i] = dp[i - 1]
        return dp[n]


ret = Solution()
print(ret.numDecodings("12"))
