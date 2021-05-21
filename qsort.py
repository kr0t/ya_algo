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


def get_pivot(array, lo, hi):
    m = (lo + hi) // 2
    result = [array[lo], array[m], array[hi]]
    for i in range(-1, len(result) - 1):
        if result[i + 1] < result[i]:
            result[i], result[i + 1] = result[i + 1], result[i]
    return result[1]


def quick_sort(array, lo, hi):
    if len(array) <= 1:
        return array
    if lo < hi:
        p = partition(array, lo, hi)
        quick_sort(array, lo, p)
        quick_sort(array, p + 1, hi)


def partition(array, lo, hi):
    p = get_pivot(array, lo, hi)
    i = lo - 1
    j = hi + 1
    while True:
        i += 1
        while array[i] < p:
            i += 1
        j -= 1
        while array[j] > p:
            j -= 1
        if i >= j:
            return j
        array[i], array[j] = array[j], array[i]


if __name__ == '__main__':
    with open('input.txt') as f:
        n = int(f.readline())
        r = []
        for i in range(n):
            name, tasks, error = f.readline().strip().split()
            r.append([-int(tasks), int(error), name])
        quick_sort(r, 0, len(r) - 1)
        names = [i[2] for i in r]
        print(*names, sep='\n')
