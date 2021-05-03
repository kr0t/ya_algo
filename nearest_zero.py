"""
ID 51240366
"""


def main():
    n = int(input())
    lst = list(map(int, input().split()))
    idx_zeros = [i for i in range(len(lst)) if lst[i] == 0]
    nearest = [0] * n
    for i in range(idx_zeros[0], len(lst), 1):
        if lst[i] == 0:
            nearest[i] = 0
        else:
            nearest[i] += nearest[i-1] + 1
    for i in range(idx_zeros[-1], 0, -1):
        if lst[i] == 0:
            nearest[i] = 0
        else:
            nearest[i] = min(nearest[i], nearest[i+1] + 1)
    for i in range(idx_zeros[0] - 1, -1, -1):
        nearest[i] += nearest[i+1] + 1
    return ' '.join([str(i) for i in nearest])


if __name__ == '__main__':
    print(main())
