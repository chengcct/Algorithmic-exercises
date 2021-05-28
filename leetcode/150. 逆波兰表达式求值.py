from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # 遇到数字进栈，遇到符号取出栈顶两个数字，并将结果压入栈
        stack = []
        for i in range(len(tokens)):
            if tokens[i] == '+' or tokens[i] == '*' or tokens[i] == '/':
                a, b = stack.pop(), stack.pop()
                if tokens[i] == '+':
                    stack.append(a + b)
                elif tokens[i] == '*':
                    stack.append(a * b)
                elif tokens[i] == '-':
                    stack.append(a - b)
                else:
                    stack.append(int(a / b))
            else:
                stack.append(int(tokens[i]))
        return stack.pop()


class Solution1:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i in '+-*/':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(str(int(eval(num2 + i + num1))))
            else:
                stack.append(i)
        return int(stack[0])


ret = Solution1()
print(ret.evalRPN(["4", "13", "5", "/", "+"]))
