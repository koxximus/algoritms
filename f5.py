"""F. Сортировка по четности
Во всех списках четные числа должны стоять на четных позициях,
а нечетные числа - на нечетных
"""
with open("input.txt") as f:
    len_arr = int(f.readline())
    arr = [int(elem) for elem in f.readline().split()]

result = [0 for _ in range(len_arr)]
i, j = 0, 1
for elem in arr:
    if elem % 2 == 0:
        result[i] = elem
        i += 2
    else:
        result[j] = elem
        j += 2

print(" ".join([str(elem) for elem in result]))
