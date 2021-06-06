"""C. Анаграммная группировка
Евлампия захотела избавиться от проблем с произношением, стать певицей, и поехать на Евровидение.
Она обратилась за помощью к логопеду. Он посоветовал ей выполнять упражнение,
которое называется анаграммная группировка.
В качестве подготовительного этапа нужно выбрать из множества строк анаграммы.
Помогите Евлампии сделать шаг к победе в песенном конкурсе.
"""
with open("input.txt") as f:
    num_words = int(f.readline())
    words = [sorted(elem) for elem in f.readline().split()]

dct = {"".join(word): [] for word in words}

for k, word in enumerate(words):
    hash_word = "".join(sorted(word))
    dct[hash_word].append(k)
for value in dct.values():
    print(" ".join(map(str, value)))


