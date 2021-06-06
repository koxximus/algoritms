with open("input.txt") as f:
    s = list(f.readline().strip("\n"))
    t = list(f.readline())

for letter in t[::-1]:
    if s and letter == s[-1]:
        s.pop()

print(s == [])
