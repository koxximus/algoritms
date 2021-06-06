"""K. Частичная сортировка
В соответствии с методом нужно разбить данные на максимально возможное количество частей таким образом,
чтобы можно было отсортировать каждую из частей отдельно, соединить,
и при этом результат будет отсортирован.
После сортировки отдельных частей менять части местами нельзя.
"""
with open("input.txt") as f:
    n = int(f.readline())
    arr = [int(elem) for elem in f.readline().split()]

cnt = 0
for i in range(1, n+1):
    if set(arr[:i]) == {elem for elem in range(i)}:
        cnt += 1

print(cnt)