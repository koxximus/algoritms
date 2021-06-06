with open("input.txt") as f:
    n = int(f.readline())
    arr_n = [int(elem) for elem in f.readline().split()]
    m = int(f.readline())
    arr_m = [int(elem) for elem in f.readline().split()]


def hash_array(array):
    n = len(array)
    return sum([array[i]*p_pow[n-1-i] for i in range(n)]) % 1073741824


p_pow = {0: 1}
for i in range(1, max(n, m)):
    p_pow[i] = p_pow[i - 1] * 257


dct = {hash_array(arr_m[i:i+1+j]): len(arr_m[i:i+1+j]) for j in range(m) for i in range(m-j)}


def find_subseq(array, m):
    for delta in range(m-1, -1, -1):
        for i in range(len(array) - delta):
            base = array[i:i + 1 + delta]
            if hash_array(base) in dct:
                return dct[hash_array(base)]
    return 0


print(find_subseq(arr_n, min(n, m)))