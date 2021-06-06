"""C. Эффективная быстрая сортировка
Рита захотела оптимизировать алгоритм быстрой сортировки.
Алгоритму не должно требоваться O(n) дополнительной памяти.
А у вас получится?
"""

with open("input.txt") as f:
    n = int(f.readline())
    arr = [int(elem) for elem in f.readline().split()]


def partition(arr, left, right):
    pivot = arr[(left + right) // 2]
    i = left-1
    j = right+1
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        j -= 1
        while arr[j] > pivot:
            j -= 1

        if i >= j:
            return j

        arr[j], arr[i] = arr[i], arr[j]


def quick_sort(nums):
    def _quick_sort(arr, l, r):
        if l < r:
            pivot = partition(arr, l, r)
            _quick_sort(arr, l, pivot)
            _quick_sort(arr, pivot+1, r)
    _quick_sort(nums, 0, len(nums)-1)


quick_sort(arr)
print(" ".join([str(elem) for elem in arr]))
