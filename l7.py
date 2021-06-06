import itertools
with open("input.txt") as f:
    n = int(f.readline())
    sum_four = int(f.readline())
    arr = sorted([int(elem) for elem in f.readline().split()])


def iterate(arr):
    yield from itertools.combinations(arr, 4)


dct = {" ".join(map(str, k)): None for k in iterate(arr) if sum(k) == sum_four}

print(len(dct))
for v in dct.keys():
    print(v)



