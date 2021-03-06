"""H. Клумбы
Евлампия захотела, чтобы у нее под окном были клумбы с одуванчиками.
Для работ по подготовке земельного участка под клумбы было нанято n садовников.
Каждый из садовников обрабатывал какой-то участок земли.
Процесс был организован не очень хорошо, иногда один и тот же участок,
или часть участка мог быть обработан сразу несколькими садовниками.
Обработанный участок любого размера становился клумбой.
В клумбе не могло быть необработанных промежутков.
Нужно определить границы получившихся клумб.
"""

with open("input.txt") as f:
    n = int(f.readline())
    fields = []
    for _ in range(n):
        fields.append([int(elem) for elem in f.readline().split()])
fields.sort()


start = 0
end = 0
i = 0

while i <= n-1:
    start = fields[i][0]
    tmp = fields[i][1]
    while (i + 1 <= n-1) and tmp >= fields[i+1][0]:
        if fields[i+1][1] > tmp:
            tmp = fields[i+1][1]
        i += 1

    end = tmp
    i += 1
    print(start, end)
