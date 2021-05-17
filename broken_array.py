"""
ID 51509910
"""


def find_elem(array, k, left, right):
    if right < left:
        return -1
    middle = (left + right) // 2
    if array[middle] == k:
        return middle
    if array[left] <= k < array[middle] or array[left] > array[middle] > k:
        return find_elem(array, k, left, middle - 1)
    else:
        return find_elem(array, k, middle + 1, right)


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        n = int(f.readline())
        elem = int(f.readline())
        arr = [int(i) for i in f.readline().split()]
    print(find_elem(arr, elem, 0, n - 1))
