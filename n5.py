"""N. Техника скорочтения
Евлампия решила научится технике скорочтения, чтобы успевать читать все выпуски любимых журналов.
Она узнала, что в основе многих техник, позволяющий быстро читать, лежит идея просматривать текст по диагонали.
Евлампия решила, что если будет чаще иметь дело с данными, которые упорядочены по диагонали,
быстрее освоит технику скорочтения.
В своем дневнике она хранит зашифрованные в виде числовых матриц записи.
Нужно отсортировать матрицы по диагонали.
"""

with open("input.txt") as f:
    strings = int(f.readline())
    columns = int(f.readline())
    matrix = [list(map(int, f.readline().split())) for _ in range(strings)]


def diagonal_sort(matrix):
    stack = []
    i, j = strings - 1, 0
    while i < strings and j < columns - 1:
        if i > 0 and j == 0:
            i -= 1
        else:
            j += 1

        while j < columns and i < strings:
            stack.append(matrix[i][j])
            i += 1
            j += 1
        stack.sort()
        i -= 1
        j -= 1
        while j >= 0 and i >= 0:
            matrix[i][j] = stack.pop()
            j -= 1
            i -= 1
        i += 1
        j += 1
    return matrix


for row in diagonal_sort(matrix):
    print(*row)
