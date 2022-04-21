# -*- coding:utf-8 -*-
# @Author : Cheng
# @Time : 2022/4/21 17:38
class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        str_list = sentence.lower().split()
        res = []
        for i, j in enumerate(str_list):
            if j.startswith(('a', 'e', 'i', 'o', 'u')):
                res.append(j + 'ma' + 'a' * (i + 1))
            else:
                res.append(j[1:]+j[:1]+'ma'+'a' * (i + 1))
        return ' '.join(res)


if __name__ == '__main__':
    s = Solution()
    print(s.toGoatLatin("I speak Goat Latin"))
