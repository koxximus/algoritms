"""A. Расписание
Помогите Алле написать код алгоритма для выбора уроков, которые пройдут в классе.
Дано расписание предметов. Нужно составить расписание,
в соответствии с которым в классе можно будет провести как можно больше уроков.
"""
with open("input.txt") as f:
    n = int(f.readline())
    lessons = []
    for i in range(n):
        lessons.append(f.readline().split())

result = []
sorted_lessons = sorted(lessons, key=lambda x: (float(x[1]), float(x[0])))
while sorted_lessons:
    if not result:
        early = sorted_lessons.pop(0)
        result.append(early)
    elif float(sorted_lessons[0][0]) >= float(result[-1][1]):
        early = sorted_lessons.pop(0)
        result.append(early)
    else:
        sorted_lessons.pop(0)

print(len(result))
for line in result:
    print(line[0], line[1])
