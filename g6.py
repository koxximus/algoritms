"""G. Минимальные суммы
Даны 2 массива, отсортированные по неубыванию, а также число k.
Нужно определить пары, которые имеют наименьшую сумму.
При этом пара должна состоять из одного элемента первого массива,
и одного элемента второго. Нужно найти k таких пар с наименьшей суммой.
"""

with open("input.txt") as f:
    len_a = int(f.readline())
    arr_a = [int(elem) for elem in f.readline().split()]
    len_b = int(f.readline())
    arr_b = [int(elem) for elem in f.readline().split()]
    k = int(f.readline())

result = []
for i in range(len_a):
    for j in range(len_b):
        result.append([arr_a[i], arr_b[j]])
result.sort(key=sum)
result = result[:k]

for i in range(k):
    result[i] = sorted(result[i])

for elem in sorted(result):
    print(*elem)
