"""
ID 51306059
"""


def main():
    n = int(input())
    lst = [int(i) for i in input().split()]
    idx_zeros = [idx for idx, value in enumerate(lst) if value == 0]
    nearest = [0] * n
    for i in range(idx_zeros[0], len(lst)):
        if lst[i] == 0:
            nearest[i] = 0
        else:
            nearest[i] += nearest[i-1] + 1
    for i in range(idx_zeros[-1], idx_zeros[0], -1):
        if lst[i] == 0:
            nearest[i] = 0
        else:
            nearest[i] = min(nearest[i], nearest[i+1] + 1)
    for i in range(idx_zeros[0] - 1, -1, -1):
        nearest[i] += nearest[i+1] + 1
    return ' '.join([str(i) for i in nearest])


if __name__ == '__main__':
    print(main())
