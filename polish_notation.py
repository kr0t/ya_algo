"""
ID 51397487
"""
OPERATORS = ['+', '-', '*', '/']

OPERATIONS = {
    '+': lambda x1, x2: x1 + x2,
    '-': lambda x1, x2: x1 - x2,
    '*': lambda x1, x2: x1 * x2,
    '/': lambda x1, x2: x1 // x2,
}


class StackIndexException(Exception):
    pass


class MyStack:
    def __init__(self):
        self.__items = []

    def __str__(self):
        return f'{self.__items}'

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        try:
            return self.__items.pop()
        except IndexError:
            raise StackIndexException

    def peek(self):
        try:
            return self.__items[-1]
        except IndexError:
            raise StackIndexException


if __name__ == '__main__':
    _stack = MyStack()
    s = input().rstrip().split()
    for i in s:
        if i not in OPERATORS:
            _stack.push(int(i))
        else:
            f = OPERATIONS[i]
            op1 = _stack.pop()
            op2 = _stack.pop()
            _stack.push(f(op2, op1))
    print(_stack.peek())
