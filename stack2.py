class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class StackMaxEffective:
    def __init__(self):
        self.head = None
        self.max_value = None

    def push(self, value):
        if self.head:
            n = Node(value)
            n.next = self.head
            self.head = n
        else:
            self.head = Node(value, self.head)
        self.max_value = max(value, self.max_value) if self.max_value is not None else value

    def pop(self):
        if self.head is None:
            print('error')
            return
        rtn = None

        if self.head:
            rtn = self.head.value
            self.head = self.head.next

        # head = self.head
        # v = head.value if head else None
        # while head:
        #     v = max(v, head.value)
        #     head = head.next
        self.max_value = max(self.head.value, self.max_value)
        return rtn

    def get_max(self):
        if self.head is None:
            print('None')
            return
        print(self.max_value)
        return


if __name__ == '__main__':
    import sys

    stack = StackMaxEffective()
    n = int(input())
    for i in range(n):
        line = sys.stdin.readline().rstrip().split()
        if line[0] == 'get_max':
            stack.get_max()
        elif line[0] == 'push':
            stack.push(int(line[1]))
        elif line[0] == 'pop':
            stack.pop()
