"""
6
1 2 4 4 6 8
1 2 3 4 5 6
3
"""


def bicycle(arr, price, left, right):
    l = right - left + 1
    if l < 1:
        return -1
    mid = (left + right) // 2
    if l == 1 and price <= arr[mid]:
        return mid + 1
    if price <= arr[mid]:
        return bicycle(arr, price, left, mid)
    else:
        return bicycle(arr, price, mid + 1, right)


if __name__ == '__main__':
    with open('input.txt') as file:
        n = int(file.readline())
        days = [int(i) for i in file.readline().strip().split()]
        price = int(file.readline())
        print(bicycle(days, price, 0, n-1), bicycle(days, 2 * price, 0, n-1))


# def sell_bike(arr, cost, start, end):
#     len_search = end - start + 1
#     if len_search < 1:
#         return -1
#     mid = (start + end) // 2
#     ind = arr[mid]
#     if len_search == 1 and cost <= int(ind):
#         return mid + 1
#     if cost <= int(ind):
#         return sell_bike(arr, cost, start, mid)
#     else:
#         return sell_bike(arr, cost, mid+1, end)
#
#
# if __name__ == '__main__':
#     with open('input.txt') as file:
#         n = int(file.readline())
#         arr = file.readline().strip().split()
#         cost = int(file.readline())
#         print(sell_bike(arr, cost, 0, n-1), sell_bike(arr, cost+cost, 0, n-1))