"""P. Собери словарь
Гоша захотел реализовать возможность собрать хеш-таблицу по двум массивам — ключам и значениям.
Ключи и значения должны идти параллельно,
то есть ключу на позиции i должно быть сопоставлено значение на позиции i или строка «None»,
если во втором массиве недостаточно элементов.
Значения, для которых нет ключей, игнорируются. Помогите Гоше справиться с этой задачей.
"""

with open("input.txt") as f:
    num_keys = int(f.readline())
    keys = f.readline().split()
    num_values = int(f.readline())
    values = f.readline().split()

dct = {key: None for key in keys}
for i in range(min(num_values, num_keys)):
    dct[keys[i]] = values[i]
for k, v in dct.items():
    print("{0}: {1}".format(k, v))
