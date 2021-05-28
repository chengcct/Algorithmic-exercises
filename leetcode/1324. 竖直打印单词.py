from typing import List


class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split(' ')
        max_len = 0
        for w in s:
            max_len = max(max_len, len(w))
        r = [[] for _ in range(max_len)]
        for w in s:
            for i in range(max_len):
                if i < len(w):
                    r[i].append(w[i])
                else:
                    r[i].append(' ')
        rr = []
        for x in r:
            rr.append(''.join(x).rstrip())
        return rr


ret = Solution()
# print(ret.printVertically("HOW ARE YOU"))
print(ret.printVertically("CONTEST IS COMING"))
