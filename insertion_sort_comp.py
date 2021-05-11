"""
3
510 56 5

565105
510565
"""


# def compare_to_number_str(first, second):
#     if len(first) == len(second) and first[0] == second[0]:
#         return int(first) < int(second)
#     else:
#         return first < second

def compare_to_number_str(first, second):
    return first < second


def sort_by_key(array):
    print(*sorted(array, key=lambda i: i * 5, reverse=True), sep='')


def insertion_sort(arr, less):
    for i in range(1, len(arr)):
        item_to_insert = arr[i]
        j = i
        while j > 0 and not less(item_to_insert, arr[j - 1]):
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = item_to_insert
    return arr


if __name__ == '__main__':
    n = int(input())
    arr = input().split()
    sort_by_key(arr)
    # print(''.join(insertion_sort(arr, compare_to_number_str)))
