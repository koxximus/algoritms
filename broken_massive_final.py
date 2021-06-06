# 33778560
with open("input.txt") as f:
    try:
        n = int(f.readline())
        desire_number = int(f.readline())
        digits = [int(elem) for elem in f.readline().split()]
    except Exception as e:
        raise Exception("Неверный формат ввода")


def idx_search(arr, pos=0):
    if len(arr) == 1 and arr[0] == desire_number:
        return pos

    elif len(arr) == 1 and arr[0] != desire_number:
        return -1

    if desire_number in set(arr[:len(arr) // 2]):
        delta = 0
        return idx_search(arr[:len(arr) // 2], pos + delta)

    elif desire_number in set(arr[len(arr) // 2:]):
        delta = len(arr) // 2
        return idx_search(arr[len(arr) // 2:], pos + delta)

    else:
        return -1


if __name__ == "__main__":
    print(idx_search(digits))
