"""N. Самый длинный палиндром
Пока ребята в Трешландии, Вася продолжает придумывать задачи про палиндром.
На этот раз необходимо узнать, палиндром какой наибольшей длины можно составить из букв данной строки.
Можно использовать только часть букв и переставлять их между собой.
"""

with open("input.txt") as f:
    string = f.readline().strip("\n")

dct = {}
for letter in string:
    if letter not in dct.keys():
        dct[letter] = 1
    else:
        dct[letter] += 1

cnt, max_elem = 0, 0
for value in sorted(dct.values(), reverse=True):
    if value == 1:
        max_elem = 1
        break
    if value % 2 == 0:
        cnt += value
    else:
        cnt += value - 1
        max_elem = 1

print(cnt + max_elem)
