class StackMax:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            print('error')
            return
        return self.items.pop()

    def get_max(self):
        if len(self.items) == 0:
            print('None')
            return
        print(sorted(self.items, reverse=True)[0])


if __name__ == '__main__':
    import sys
    stack = StackMax()
    n = int(input())
    for i in range(n):
        line = sys.stdin.readline().rstrip().split()
        if line[0] == 'get_max':
            stack.get_max()
        elif line[0] == 'push':
            stack.push(int(line[1]))
        elif line[0] == 'pop':
            stack.pop()
