from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def rot_at(s, i, move):
            return s[:i] + str((int(s[i]) + move + N) % N) + s[i + 1:]

        vis, q1, q2 = set(deadends), set(), set()
        LEN, N, step = len(target), 10, 0
        q1.add('0000')
        q2.add(target)
        # 单独处理初始无解情况
        if '0000' in vis:
            return -1
        while q1:
            temp = set()  # 创建临时set，保存下层的所有结果
            for cur in q1:
                # check
                if cur in q2:
                    return step  # 如果双向BFS相遇
                vis.add(cur)
                # put all node into q
                for i in range(LEN):
                    t = rot_at(cur, i, +1)
                    if t not in vis:
                        temp.add(t)

                    t = rot_at(cur, i, -1)
                    if t not in vis:
                        temp.add(t)
            step += 1
            # 交替探测，谁节点少优先检测
            if len(q2) < len(temp):
                q1 = q2
                q2 = temp
            else:
                q1 = temp
        return -1


ret = Solution()
print(ret.openLock(["0201", "0101", "0102", "1212", "2002"], "0202"))
