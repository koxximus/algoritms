"""C. Эффективные числа Фибоначчи
У многих жителей Трешландии на компьютере осталось совсем мало свободного места.
Но они тоже хотят иметь возможность вычислять, сколько животных могут завести.
Нужно оптимизировать решение задачи про вычисление чисел Фибоначчи.
Объем дополнительной памяти должен быть O(1).
"""
with open("input.txt") as f:
    n = int(f.readline())

def fib(n, s=1, f=1):
    if n in (0, 1):
        return s
    return fib(n-1, s+f, s)


print(fib(n))