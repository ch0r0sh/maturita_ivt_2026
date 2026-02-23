from random import randint

SIZE = 10 ** 5
RANGE = 10 ** 5


def partition(data, start, end):
    pivot = end
    i = start - 1

    # find the first element that is larger than pivot
    for j in range(start, end + 1):
        if data[j] >= data[pivot]:
            i = j
            break

    for j in range(i + 1, end):
        if data[j] <= data[pivot]:
            data[i], data[j] = data[j], data[i]
            i += 1

    data[i], data[pivot] = data[pivot], data[i]
    return i


def quicksort(data, start, end):
    if start >= end:
        return

    pivo = partition(data, start, end)
    quicksort(data, start, pivo - 1)
    quicksort(data, pivo + 1, end)


data = [randint(1, RANGE) for _ in range(SIZE)]
quicksort(data, 0, len(data) - 1)
print(data)
