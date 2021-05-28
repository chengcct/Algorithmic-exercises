class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        mod = 10 ** 9 + 7

        for i in range(1, n + 1):
            for j in range(i - 1, -1, -1):
                if s[j] == '0':
                    continue
                if int(s[j:i]) <= k:
                    dp[i] += dp[j]
                else:
                    if s[i - 1] == '0' and dp[i] == 0:
                        return 0
                    break
            dp[i] %= mod
        return dp[-1] % mod


ret = Solution()
print(ret.numberOfArrays("1317", 2000))
