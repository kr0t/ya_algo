"""
[11, 2, 9, 7, 1]
"""


def insertion_sort(arr):
    for i in range(1, len(arr)):
        item_to_insert = arr[i]
        j = i
        while j > 0 and item_to_insert < arr[j - 1]:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = item_to_insert
    return arr


if __name__ == '__main__':
    print(insertion_sort([11, 2, 9, 7, 1]))
