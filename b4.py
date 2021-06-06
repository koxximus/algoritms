"""B. Фибоначчи с памятью
Функция из прошлого задания работала слишком долго.
Нужно модифицировать ее таким образом,
чтобы одни и те же значения повторно не вычислялись.
"""
with open("input.txt") as f:
    n = int(f.readline())

fibo = [1, 1]


def fib(n):
    if n in range(0, len(fibo)):
        return fibo[n]
    fibo.append(fib(n-1)+fib(n-2))
    return fibo[n]


print(fib(n))
