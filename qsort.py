"""
algorithm quicksort(A, lo, hi) is
    if lo < hi then
        p := partition(A, lo, hi)
        quicksort(A, lo, p)
        quicksort(A, p + 1, hi)

algorithm partition(A, lo, hi) is
    pivot := A[ floor((hi + lo) / 2) ]
    i := lo - 1
    j := hi + 1
    loop forever
        do
            i := i + 1
        while A[i] < pivot
        do
            j := j - 1
        while A[j] > pivot
        if i ≥ j then
            return j
        swap A[i] with A[j]
"""


def quick_sort(array, lo, hi):
    if lo < hi:
        p = partition(array, lo, hi)
        quick_sort(array, lo, p)
        quick_sort(array, p + 1, hi)


def partition(array, lo, hi):
    p = (hi + lo) // 2
    i = lo - 1
    j = hi + 1
    while True:
        i += 1
        while array[i] < array[p]:
            i += 1
        j -= 1
        while array[j] > array[p]:
            j -= 1
        if i >= j:
            return j
        array[i], array[j] = array[j], array[i]


if __name__ == '__main__':
    arr = [22, 5, 1, 18, 99]
    quick_sort(arr, 0, len(arr) - 1)
    print(arr)



def sort_obj(first, second):
    if first[0] == second[0] and first[1] == second[1]:
        return first if first > second else second
    if first[0] == second[0] and first[1] < second[1]:
        return first

