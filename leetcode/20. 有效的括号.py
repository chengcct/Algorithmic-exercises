class Solution:
    def isValid(self, s: str) -> bool:
        left = ['(', '{', '[']
        dic = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for ele in s:
            if ele in left:
                stack.append(ele)
            elif stack and ele == dic[stack[-1]]:
                stack.pop()
            else:
                return False
        return not stack


ret = Solution()
print(ret.isValid("()"))
