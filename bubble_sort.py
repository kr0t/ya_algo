"""
4 3 9 2 1
1 1 1 1 1
"""


def bubble_sort(arr):
    flag = False
    changed = True
    while changed:
        changed = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                changed = True
                flag = True
        if changed:
            print(*arr)
    if not flag:
        print(*arr)
    return arr


if __name__ == '__main__':
    n = int(input())
    arr = [int(i) for i in input().split()]
    bubble_sort(arr)
