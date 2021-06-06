"""E. Печеньки
К Васе в гости пришли одноклассники. Его мама решила угостить ребят печеньем.
Но не всё так просто. Печенья могут быть разного размера.
У каждого ребёнка есть фактор жадности — минимальный размер печенья,
которое он возьмёт. Нужно выяснить, сколько ребят останутся довольными.
Каждый ребёнок может взять не больше одного печенья.
"""
with open("input.txt") as f:
    n = int(f.readline())
    factor = sorted(list(map(int, f.readline().split())), reverse=True)
    m = int(f.readline())
    sizes = sorted(list(map(int, f.readline().split())))


happy_child = 0

for i in range(len(factor)):
    if sizes and factor[i] <= sizes[-1]:
        sizes.pop()
        happy_child += 1

print(happy_child)
