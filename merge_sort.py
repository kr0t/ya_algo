# def merge_sort(array):
#     if len(array) == 1:
#         return array
#
#     left = merge_sort(array[0:len(array)//2])
#     right = merge_sort(array[len(array)//2:len(array)])
#
#     result = [] * len(array)
#
#     l, r, k = 0, 0, 0
#
#     while l < len(left) and r < len(right):
#         if left[l] <= right[r]:
#             result[k] = left[l]
#             l += 1
#         else:
#             result[k] = right[r]
#             r += 1
#         k += 1
#
#     while l < len(left):
#         result[k] = left[l]
#         l += 1
#         k += 1
#     while r < len(right):
#         result[k] = right[l]
#         r += 1
#         k += 1
#
#     return result

def merge_sort(array):
    if len(array) == 1: return array

    # запускаем сортировку рекурсивно на левой половине
    left = merge_sort(array[0: len(array) // 2])

    # запускаем сортировку рекурсивно на правой половине
    right = merge_sort(array[len(array) // 2: len(array)])

    # заводим массив для результата сортировки
    result = [None] * len(array)

    # сливаем результаты
    l, r, k = 0, 0, 0
    while l < len(left) and r < len(right):
        # выбираем, из какого массива забрать минимальный элемент
        if left[l] <= right[r]:
            result[k] = left[l]
            l += 1
        else:
            result[k] = right[r]
            r += 1
        k += 1

    # Если один массив закончился раньше, чем второй, то
    # переносим оставшиеся элементы второго массива в результирующий
    while l < len(left):
        result[k] = left[l]  # перенеси оставшиеся элементы left в result
        l += 1
        k += 1
    while r < len(right):
        result[k] = right[r]  # перенеси оставшиеся элементы right в result
        r += 1
        k += 1

    return result


if __name__ == '__main__':
    print(merge_sort([3, 5, 6, 2, 7, 22, 4, 5, 88, 6, 0, 2, 4, 43]))
