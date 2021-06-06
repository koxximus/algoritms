"""D. Соседи
Дана матрица. Нужно написать функцию, которая для элемента возвращает всех его соседей.
Соседним считается элемент, находящийся от текущего на одну ячейку влево, вправо,
вверх или вниз. Диагональные элементы соседними не считаются.
"""
with open('input.txt') as f:
    n = int(f.readline())
    m = int(f.readline())
    matrix = []
    for i in range(n):
        matrix.append(f.readline().split())

    y = int(f.readline())
    x = int(f.readline())

neibors = []

a = y - 1
b = x
if a > -1:
    neibors.append(int(matrix[a][b]))

a = y + 1
b = x
if a < n:
    neibors.append(int(matrix[a][b]))

a = y
b = x - 1
if b > -1:
    neibors.append(int(matrix[a][b]))

a = y
b = x + 1
if b < m:
    neibors.append(int(matrix[a][b]))

print(*sorted(neibors))
