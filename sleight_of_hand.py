"""
ID 51305900
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
    print(len([i for i in counter if i[1] <= 2 * k]))


if __name__ == '__main__':
    main()
