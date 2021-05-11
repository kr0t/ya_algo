"""
ID 51397289
"""
import sys


class DequeSizeException(Exception):
    pass


class Deque:
    def __init__(self, n):
        self.__queue = [None] * n
        self.__max_n = n
        self.__head = 0
        self.__tail = 0
        self.__deque_size = 0

    def __str__(self):
        return f'Deque({self.__max_n})'

    def is_not_full(self):
        return self.__deque_size != self.__max_n

    def is_empty(self):
        return self.__deque_size == 0

    def push_back(self, item):
        if self.is_not_full():
            self.__queue[self.__tail] = item
            self.__tail = (self.__tail + 1) % self.__max_n
            self.__deque_size += 1
        else:
            raise DequeSizeException

    def pop_back(self):
        if self.is_empty():
            raise DequeSizeException
        x = self.__queue[self.__tail - 1]
        self.__queue[self.__tail - 1] = None
        self.__tail = (self.__tail - 1) % self.__max_n
        self.__deque_size -= 1
        return x

    def push_front(self, item):
        if self.is_not_full():
            self.__queue[self.__head - 1] = item
            self.__head = (self.__head - 1) % self.__max_n
            self.__deque_size += 1
        else:
            raise DequeSizeException

    def pop_front(self):
        if self.is_empty():
            raise DequeSizeException
        x = self.__queue[self.__head]
        self.__queue[self.__head] = None
        self.__head = (self.__head + 1) % self.__max_n
        self.__deque_size -= 1
        return x

    def size(self):
        return self.__deque_size


if __name__ == '__main__':

    n = int(input())
    m = Deque(int(input()))

    ACTIONS = {
        'push_back': lambda x: m.push_back(x),
        'push_front': lambda x: m.push_front(x),
        'pop_front': lambda: m.pop_front(),
        'pop_back': lambda: m.pop_back()
    }

    for i in range(n):
        command, *arg = sys.stdin.readline().rstrip().split()
        try:
            f = ACTIONS[command]
            if arg:
                f(int(arg[0]))
            else:
                print(f())
        except DequeSizeException:
            print('error')
