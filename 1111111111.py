with open("input.txt") as f:
    number_quantity = int(f.readline())
    numbers = f.readline().split()

buckets = [[] for _ in range(10)]
n = len(max(numbers, key=int))

for i in range(number_quantity):
    if len(numbers[i]) < n:
        numbers[i] = "0" * (n - len(numbers[i])) + numbers[i]


def buckets_add(arr, q_radix):
    for num in arr:
        buckets[int(num[q_radix])].append(arr.pop())
    return buckets


def buckets_pop(arr):
    for bucket in range(10):
        for _ in range(len(arr[bucket])):
            if arr[bucket]:
                number_from_bucket = buckets[bucket].pop()
                numbers.append(number_from_bucket)


def radix_sort(arr, q_radix):
    if q_radix == -1:
        return arr
    else:
        buckets_pop(buckets_add(arr, q_radix))
        return radix_sort(arr, q_radix - 1)


for number in (radix_sort(numbers, n - 1)):
    while number[0] == "0" and len(number) > 1:
        number = number.replace("0", "", 1)
    print(number, end=" ")
