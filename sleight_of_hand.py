"""
ID 51241536
"""
import sys
from collections import Counter


def main():
    k = int(input())
    fields = []
    for i in range(4):
        line = sys.stdin.readline().rstrip()
        fields += [int(i) for i in line if i != '.']
    counter = Counter(fields).most_common()
    print(len(list(filter(lambda x: x[1] <= 2 * k, counter))))


if __name__ == '__main__':
    main()
