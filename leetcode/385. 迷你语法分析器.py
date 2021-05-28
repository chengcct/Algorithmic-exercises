# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
    def __init__(self, value=None):
        """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """

    def isInteger(self):
        """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

    def add(self, elem):
        """
       Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
       :rtype void
       """

    def setInteger(self, value):
        """
       Set this NestedInteger to hold a single integer equal to value.
       :rtype void
       """

    def getInteger(self):
        """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """

    def getList(self):
        """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """


class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if s[0] != '[':
            return NestedInteger(int(s))
        if s == '[]':
            return NestedInteger()
        stack = []
        tmp = ''

        for i, ch in enumerate(s):
            if ch == '[':
                stack.append(NestedInteger())
            elif ch == ',':
                if s[i - 1] != ']':
                    num = int(tmp)
                    stack[-1].add(NestedInteger(num))
                    tmp = ''
            elif ch == ']':
                if s[i - 1] != ']':
                    if s[i - 1] != '[':
                        num = int(tmp)
                        stack[-1].add(NestedInteger(num))
                if len(stack) > 1:
                    top = stack.pop()
                    stack[-1].add(top)
                tmp = ''
            else:
                tmp += ch
        return stack[0]


class Solution1:
    def deserialize(self, s: str) -> NestedInteger:
        stack = []
        num, sign, is_num = 0, 1, False
        if s[0] != '[':
            return NestedInteger(int(s))
        for i in s:
            if i.isdigit():
                num = num * 10 + int(i)
                is_num = True
            elif i == '[':
                stack.append(NestedInteger())
            elif i == '-':
                sign = -1
            elif i == ',' or i == ']':
                if is_num:
                    stack[-1].add(NestedInteger(sign * num))
                num, sign, is_num = 0, 1, False
                if i == ']' and len(stack) > 1:
                    curList = stack.pop()
                    stack[-1].add(curList)
        return stack[0]
