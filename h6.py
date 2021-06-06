with open("input.txt") as f:
    len_a = int(f.readline())
    arr = [int(elem) for elem in f.readline().split()]
    k = int(f.readline())

import heapq

def heapsort(iterable, k):
    h = []
    j = 1
    while j < len(iterable):
        for i in range(j, len(iterable)):
            h.append(abs(iterable[i] - iterable[i - j]))
        j += 1
    return sorted(h)[k-1]
print(heapsort(arr, k))
