# -*- coding:utf-8 -*-
# @Author : Cheng
# @Time : 2022/5/13 17:32
class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        if abs(len(first) - len(second)) > 1:
            return False
        if len(first) > len(second):
            first, second = second, first
        for i in range(len(first)):
            if first[i] != second[i]:
                if len(first) == len(second):
                    return first[i + 1:] == second[i + 1:]
                else:
                    return first[i:] == second[i + 1:]
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.oneEditAway('pale', 'ple'))
    print(solution.oneEditAway('pales', 'pale'))
    print(solution.oneEditAway('pale', 'bale'))
    print(solution.oneEditAway('pale', 'bake'))
    print(solution.oneEditAway('pale', 'pale'))
    print(solution.oneEditAway('pale', 'bae'))
