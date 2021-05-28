from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # main和max函数对字符串排序
        # 是对字符串中的字母的ASCII值进行安位排序的
        # 即对每个位比大小
        # 例如abc(97 98 99)、abb(97 98 98)、acc(97 99 99)
        # 则顺序为 abb < abc < acc
        # 比较排序中最大值和最小值
        # 最大值与最小值的前缀字母有几个一样的，则有整个字符串有几个相同的前缀
        # 因为：若最大值与最小值在同一位的字母一样，则ASCII值相等
        # 这说明中间字符串该位的ASCII值也相等（夹逼定理）
        # 若最大和最小值在同一位的值不等，则结束

        if not strs:
            return ""
        s1 = min(strs)
        s2 = max(strs)
        for i, x in enumerate(s1):
            if x != s2[i]:
                return s2[:i]
        return s1


ret = Solution()
print(ret.longestCommonPrefix(["flower", "flow", "flight"]))
