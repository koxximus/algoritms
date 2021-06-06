"""L. Банкомат
Тимофей пошел снять деньги в банкомат. Ему нужно n трешландийских долларов.
В банкомате в бесконечном количестве имеется n монет различных достоинств.
Нужно определить число способов, которыми Тимофей сможет набрать нужную сумму.
Тимофей пошел снять деньги в банкомат. Ему нужно n трешландийских долларов.
В банкомате в бесконечном количестве имеется n монет различных достоинств.
Нужно определить число способов,
которыми Тимофей сможет набрать нужную сумму.

"""
with open("input.txt") as file:
    m_summ = int(file.readline())
    n_coins = int(file.readline())
    coins = list(map(int, file.readline().split()))


def cc(amount, quantity):
    if amount == 0:
        return 1
    if amount < 0 or quantity == 0:
        return 0
    else:
        return cc(amount, quantity-1)+cc(amount-coins[quantity-1], quantity)

print(cc(m_summ, n_coins))
