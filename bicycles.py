def bicycle(arr, price, left, right):
    if right <= left:
        return -1
    mid = (left + right) // 2
    if arr[mid] == price:
        return mid
    elif price < arr[mid]:
        return bicycle(arr, price, left, right)
    else:
        return bicycle(arr, price, mid + 1, right)


if __name__ == '__main__':
    n = int(input())
