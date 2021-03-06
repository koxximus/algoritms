"""B. Легкие числа
Евлампия в школе не очень любила арифметику. Ей кажется, что считать очень сложно.
Как-то она услышала, что бывают простые числа.
Евлампия подумала, что, используя их, считать намного проще.
На день рождения она попросила отца в качестве подарка разрешить жителям Трешландии использовать только простые числа,
и называть их легкими числами, так как букву "Р" она плохо выговаривает.
Помогите жителям Трешландии определить, сколько чисел, не превышающих определенное число, они могут использовать.
"""
with open("input.txt") as f:
    n = int(f.readline())


def get_smaller_primes_linear(n):
    lp = [0] * (n + 1)
    primes = []
    for i in range(2, n):
        if lp[i] == 0:
            lp[i] = i
            primes.append(i)
        for p in primes:
            if (p > lp[i]) or (p * i > n):
                break
            lp[p * i] = p
    return primes[-1]


print(get_smaller_primes_linear(n))
