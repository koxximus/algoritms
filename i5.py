"""I. Гардероб
Евлампия решила оставить у себя в гардеробе вещи только трех цветов:
розового, желтого, и малинового.
Она захотела отсортировать одежду по цветам.
Сначала должны идти вещи розового цвета(0), далее - желтого(1),
и в конце - малинового(2). Помогите Евлампии навести порядок в гардеробе.
"""
with open("input.txt") as f:
    n = int(f.readline())
    clothes = f.readline().split()

pink = []
yellow = []
crimson = []

for i in range(n):
    if clothes[i] < "1":
        pink.append(clothes[i])
    elif clothes[i] > "1":
        crimson.append(clothes[i])
    else:
        yellow.append(clothes[i])

print(" ".join(pink+yellow+crimson))
