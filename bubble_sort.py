"""
4 3 9 2 1
"""


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                print(arr)


if __name__ == '__main__':
    print(bubble_sort([4, 3, 9, 2, 1]))
