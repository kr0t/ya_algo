"""
ID 51329618
"""

import sys


class Deque:
    def __init__(self, n):
        self.queue = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.deque_size = 0

    def __str__(self):
        return f'Deque({self.max_n})'

    def is_empty(self):
        return self.deque_size == 0

    def push_back(self, item):
        if self.deque_size != self.max_n:
            self.queue[self.tail] = item
            self.tail = (self.tail + 1) % self.max_n
            self.deque_size += 1
        else:
            print('error')

    def pop_back(self):
        if self.is_empty():
            print('error')
            return
        x = self.queue[self.tail - 1]
        self.queue[self.tail - 1] = None
        self.tail = (self.tail - 1) % self.max_n
        self.deque_size -= 1
        print(x)

    def push_front(self, item):
        if self.deque_size != self.max_n:
            self.queue[self.head - 1] = item
            self.head = (self.head - 1) % self.max_n
            self.deque_size += 1
        else:
            print('error')

    def pop_front(self):
        if self.is_empty():
            print('error')
            return
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.deque_size -= 1
        print(x)

    def size(self):
        print(self.deque_size)


if __name__ == '__main__':

    n = int(input())
    m = Deque(int(input()))

    for i in range(n):
        line = sys.stdin.readline().rstrip().split()
        if line[0] == 'push_back':
            m.push_back(int(line[1]))
        elif line[0] == 'push_front':
            m.push_front(int(line[1]))
        elif line[0] == 'pop_front':
            m.pop_front()
        elif line[0] == 'pop_back':
            m.pop_back()
