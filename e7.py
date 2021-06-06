with open("input.txt") as f:
    rounds = int(f.readline())
    result = [int(elem) for elem in f.readline().split()]

summa = sum(result)
max_q = 2*min(summa, rounds - summa)


def search(result, max_q):
    for i in range(len(result)-max_q+1):

        if 2*sum(result[i:i+max_q]) == len(result[i:i+max_q]):
            return len(result[i:i+max_q])

    else:
        max_q -= 2
        return search(result, max_q)


print(search(result, max_q))
