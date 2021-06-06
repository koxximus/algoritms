"""O. Периметр
Кондратий решил устроить соревнование. Билет на выставку его картин получит тот,
кто напишет самую эффективную программу, решающую следующую задачу.
На клетчатом поле из нулей нарисована некоторая фигура из единичек.
Известно, что внутри фигуры нет пробелов (то есть участков из нулей), то есть она односвязная.
Найдите периметр этой фигуры, каждая сторона клетки имеет длину 1.
Стороны клеток, лежащие на границе поля, также надо учитывать.
"""
with open("input.txt") as f:
    rows, colomns = [int(elem) for elem in f.readline().split()]
    picture = [[int(elem) for elem in f.readline().split()] for _ in range(rows)]

perimetr = 0
for i in range(rows):
    one_in_row = False
    for j in range(colomns):
        if picture[i][j] == 1:
            one_in_row = True
            perimetr += 2
            if i + 1 < rows:
                perimetr -= picture[i + 1][j]
            if i - 1 >= 0:
                perimetr -= picture[i - 1][j]
    if one_in_row:
        perimetr += 2

print(perimetr)
