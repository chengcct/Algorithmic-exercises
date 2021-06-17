"""栈"""


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        return self.stack.pop()

    def get_top(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None

    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False


def bra(exp):
    stk = Stack()
    for ch in exp:
        if ch in ['(', '[']:
            stk.push(ch)
        elif ch in [')', ']']:
            if stk.isEmpty():
                return False
            chFormStack = stk.pop()
            if ch == ']' and chFormStack != '[' or ch == ')' and chFormStack != '(':
                return False
    return stk.isEmpty()


def main():
    exp = input('输入吧')
    if bra(exp):
        print('OK')
    else:
        print('Not ok')


if __name__ == '__main__':
    main()
