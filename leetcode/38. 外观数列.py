class Solution:
    def countAndSay(self, n: int) -> str:
        res = '1'
        for _ in range(n - 1):
            p, q = 0, 1
            tmp = ''
            while q <= len(res):
                if q == len(res):
                    tmp = tmp + str(q - p) + res[p]
                elif res[q] != res[p]:
                    tmp = tmp + str(q - p) + res[p]
                    p = q
                q += 1
            res = tmp
        return res


ret = Solution()
print(ret.countAndSay(4))
