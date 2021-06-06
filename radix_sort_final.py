# 33869013
with open("input.txt") as f:
    try:
        number_quantity = int(f.readline())
        numbers = f.readline().split()
    except Exception as e:
        raise Exception("Неверный формат ввода")

buckets = [[] for _ in range(10)]
n = len(max(numbers, key=int))


def buckets_add(arr, q_radix):
    for number in arr[::-1]:
        if len(number) < abs(q_radix):
            ind = 0
        else:
            ind = int(number[q_radix])
        buckets[ind].append(arr.pop())
    return buckets


def buckets_pop(arr):
    for bucket in range(10):
        for _ in range(len(arr[bucket])):
            if arr[bucket]:
                number_from_bucket = buckets[bucket].pop()
                numbers.append(number_from_bucket)


def radix_sort(arr, q_radix):
    if q_radix < -n:
        return arr
    else:
        buckets_pop(buckets_add(arr, q_radix))
        return radix_sort(arr, q_radix - 1)


if __name__ == "__main__":
    print(" ".join(radix_sort(numbers, - 1)))
