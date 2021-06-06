"""H. Генератор скобок
В Удотинске объявлен конкурс. Нужно написать самую быструю реализацию функции,
которая генерирует все правильные скобочные последовательности длины n.
Вид скобок только один: ( )
"""
with open("input.txt") as f:
    n = int(f.readline())

balance = 0
stack = [None for __ in range(n*2)]
ind = 0


def generate_seq(n, balance, ind, stack):
    if balance <= n*2 - ind - 2:
        stack[ind] = "("
        generate_seq(n, balance+1, ind+1, stack)
    if balance > 0:
        stack[ind] = ")"
        generate_seq(n, balance-1, ind+1, stack)
    if ind == n*2:
        if balance == 0:
            print("".join(stack))


generate_seq(n, balance, ind, stack)
