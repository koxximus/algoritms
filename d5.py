"""D. Тараканьи бега
Есть два списка со стартовыми номерами тараканов.
Нужно вывести номера, которые встречаются и в первом,
и во втором списке. Квадратичный алгоритм не подойдет для этой задачи.
Тараканы разбегутся, пока алгоритм закончит работу.
"""
with open("input.txt") as f:
    len_first_arr = int(f.readline())
    len_second_arr = int(f.readline())
    first_arr = f.readline().split()
    second_arr = f.readline().split()


second_set = set(second_arr)
for bug in first_arr:
    if bug in second_set:
        print(bug, end=" ")
        second_set.discard(bug)

