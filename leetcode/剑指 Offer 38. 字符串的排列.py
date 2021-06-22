from typing import List


class Solution:
    def permutation(self, s: str) -> List[str]:
        s, res, tmp = list(s), list(), list()
        s.sort()

        def dfs(s):
            if len(s) == 0:
                res.append(''.join(tmp))
                return
            for i, j in enumerate(s):
                if i > 0 and s[i] == s[i - 1]:
                    continue
                s.pop(i)
                tmp.append(j)
                dfs(s)
                s.insert(i, j)
                tmp.pop(-1)

        dfs(s)
        return res


if __name__ == '__main__':
    res = Solution()
    print(res.permutation('abc'))
