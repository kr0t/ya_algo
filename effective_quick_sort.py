def is_better(first, second):
    if first[1] == second[1]:
        if first[2] == second[2]:
            return first[0] < second[0]
        return first[2] < second[2]
    return first[1] > second[1]


def quick_sort(array, lo, hi):
    if lo < hi:
        p = partition(array, lo, hi)
        quick_sort(array, lo, p)
        quick_sort(array, p + 1, hi)


def partition(array, lo, hi):
    p = (hi + lo) // 2
    # i = lo - 1
    i = lo
    # j = hi + 1
    j = hi
    while True:
        # i += 1
        # while array[i] > array[p] < array[i]:
        while array[i] > array[p] and is_better(array[i], array[p]):
            i += 1
        # j -= 1
        # while array[j] < array[p] > array[j]:
        while array[j] < array[p] and is_better(array[p], array[j]):
            j -= 1
        if i >= j:
            return j
        array[i], array[j] = array[j], array[i]


if __name__ == '__main__':
    with open('input.txt') as f:
        n = int(f.readline())
        print(n)
        r = []
        for i in range(n):
            name, tasks, error = f.readline().strip().split()
            r.append((int(tasks), int(error), name))
            # r.append((int(tasks), int(error)))
        quick_sort(r, 0, len(r) - 1)
        print(r)
