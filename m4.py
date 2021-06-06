"""M. Земельный участок
Помогите Овощеславу определить максимально возможный размер квадратных участков,
на которые он может разделить свои владения.
"""
with open("input.txt") as f:
    width = int(f.readline())
    length = int(f.readline())


def max_size(w, l):
    if w % l == 0:
        return l
    else:
        return max_size(l, w%l)


print(max_size(width, length))
