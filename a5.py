"""A. Пузырек
На каждом шаге проходим по массиву поочередно сравниваем пары соседних элементов.
Если элемент на позиции i больше элемента на позиции i+1, меняем их местами.
После первой итерации самый большой элемент окажется в конце массива.
Проходим по массиву, выполняя указанные действия n - 1 раз, или до тех пор,
пока на очередной итерации не окажется, что обмены больше не нужны,
то есть массив уже отсортирован.
"""
with open("input.txt") as f:
    n = int(f.readline())
    arr = [int(elem) for elem in f.readline().split()]

for j in range(n):
    for i in range(n-1-j):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]

print(" ".join([str(elem) for elem in arr]))
