with open("input.txt") as f:
    a = int(f.readline())
    m = int(f.readline())
    string = f.readline().strip("\n")

def fill_p_pow(a,n):
    for i in range(1, n):
        p_pow[i] = p_pow[i - 1] * a
        yield p_pow[i]

p_pow = {0: 1}
n = len(string)
h = ord(string[-1])
h += sum([ord(string[-i-2])*a for i, a in enumerate(fill_p_pow(a, n))])
print(h%m)