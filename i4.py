"""I. Призы
В конкурсе на самую быструю программу сортировки одинаковый результат получили k человек.
В призовом фонде имеется n монет различного достоинства. Нужно определить,
можно ли разделить их между победителями таким образом, чтобы каждый получил одинаковую сумму.
"""
with open("input.txt") as f:
    n = int(f.readline())
    k = int(f.readline())
    nominals = list(map(int, f.readline().split()))


def check():
    if sum(nominals) % n != 0:
        return False
    else:
        personal_prize = int(sum(nominals) / n)
        return grant_prize(0, 0, 0, personal_prize)


def grant_prize(cnt, summ, i, pp):
    if summ == pp:
        return grant_prize(cnt+1, 0, 0, pp)
    if not nominals or cnt == n:
        return cnt == n
    elif i+1 <= len(nominals) and summ + nominals[i] > pp:
        return grant_prize(cnt, summ, i+1, pp)
    elif i+1 <= len(nominals):
        y = nominals.pop(i)
        return grant_prize(cnt, summ + y, i, pp)
    return False


print(check())
