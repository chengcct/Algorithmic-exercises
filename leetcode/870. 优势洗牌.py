from typing import List


class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        res = []
        # 降序排列
        A.sort(reverse=True)
        # B的索引与值组成元组
        b = []
        for i in range(len(B)):
            b.append((i, B[i]))
        # 对b降序排列
        b.sort(key=lambda x: x[1], reverse=True)
        # 从A的后面开始弹元素s，如果元素s比b中最后一个元素例如：（min的min[1]）大的话，就将A中弹出的s(int)和m(tuple)组成一个元组，反之就将s与b中第一个元素例如：（max的max[1]）,组成元组添加入res中，最后形成[(2, (0, 1)), (7, (2, 4)), (11, (1, 10)), (15, (3, 11))]
        while A:
            s = A.pop()
            if s > b[-1][1]:
                res.append((s, b.pop()))
            else:
                res.append((s, b.pop(0)))
        res.sort(key=lambda x: x[1][0])
        return [i[0] for i in res]


ret = Solution()
print(ret.advantageCount([2, 7, 11, 15], [1, 10, 4, 11]))
