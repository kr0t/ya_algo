"""
ID 51332482
"""


class myStack:
    def __init__(self):
        self.items = []

    def __str__(self):
        return f'{self.items}'

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]


if __name__ == '__main__':
    _stack = myStack()
    operators = ['+', '-', '*', '/']
    s = input().rstrip().split()
    for i in s:
        if i not in operators:
            _stack.push(int(i))
        else:
            if i == '+':
                op1 = _stack.pop()
                op2 = _stack.pop()
                _stack.push(op2 + op1)
            elif i == '-':
                op1 = _stack.pop()
                op2 = _stack.pop()
                _stack.push(op2 - op1)
            elif i == '*':
                op1 = _stack.pop()
                op2 = _stack.pop()
                _stack.push(op2 * op1)
            elif i == '/':
                op1 = _stack.pop()
                op2 = _stack.pop()
                _stack.push(op2 // op1)
    print(_stack.peek())
