import collections


class Solution:
    def customSortString(self, S: str, T: str) -> str:
        # 利用counter初始化时保留元素出场顺序的特点，按照S优先处理即可
        cs = collections.Counter(S)
        ct = collections.Counter(T)
        return ''.join(list((cs + ct - cs).elements()))


ret = Solution()
print(ret.customSortString("cba", "abcd"))
