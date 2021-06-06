"""D. Ценный рюкзак
Реализуйте код алгоритма заполнения рюкзака, рассмотренного в лекции.
"""

with open("input.txt") as f:
    m = int(f.readline())
    n = int(f.readline())
    goods = []
    for i in range(n):
        goods.append(list(map(int, f.readline().split())))

sorted_goods = sorted(goods, key=lambda x: (-x[0], x[1]))

bag = []
weight = 0

for good in sorted_goods:
    if not bag and good[1] <= m:
        bag.append(good)
        weight += good[1]
    elif good[1] + weight <= m:
        bag.append(good)
        weight += good[1]


print(*sorted([goods.index(good) for good in bag]), end=" ")
