"""I. Одинаковые суммы
Гоше стало интересно,
можно ли разбить все заработанные им во время игры в Лампу очки на две части так,
чтобы сумма в них была одинаковой.
"""
with open("input.txt") as f:
    n = int(f.readline())
    points = list(map(int, f.readline().split()))
from functools import reduce


def half_sum(points):
    sum_all = reduce(lambda x, y: abs(x - y), sorted(points, reverse=True))
    print(sum_all)
    return sum_all == 0


print(half_sum(points))
