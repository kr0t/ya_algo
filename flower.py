"""
4
7 8
7 8
2 3
6 10
"""


def flower(f):
    result = []
    curr = f[0]
    for c in f[1:]:
        if curr[1] < c[0]:
            result.append(curr)
            curr = c
    result.append(curr)
    print(result)


if __name__ == '__main__':
    # n = int(input())
    flowers = []
    with open('input.txt', 'r') as f:
        n = int(f.readline().strip())
        for i in range(n):
            start, end = f.readline().strip().split()
            flowers.append([int(start), int(end)])
    flowers.sort()
    flower(flowers)
