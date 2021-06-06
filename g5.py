"""G. Периметр треугольника
Перед сном Рита решила поиграть в игру на телефоне. Дан массив целых чисел,
 в котором каждый элемент обозначает длину стороны треугольника.
 Нужно определить максимально возможный периметр треугольника,
 составленного из сторон с длинами из заданного массива.
Помогите Рите скорее закончить игру и пойти спать.
"""
with open("input.txt") as f:
    len_arr = int(f.readline())
    arr = sorted([int(elem) for elem in f.readline().split()], reverse=True)

max_p = 0
for i in range(len_arr-2):
    if arr[i] < arr[i+1] + arr[i+2]:
        max_p = arr[i]+arr[i+1]+arr[i+2]
        break

print(max_p)
