"""B. Сортировка вставками
"""
with open("input.txt") as f:
    n = int(f.readline())
    arr = [int(elem) for elem in f.readline().split()]

for i in range(1, n):
    tmp = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > tmp:
        arr[j+1] = arr[j]
        j -= 1
    arr[j + 1] = tmp

print(" ".join([str(elem) for elem in arr]))
