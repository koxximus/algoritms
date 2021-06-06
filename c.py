"""C. Подстроки
На вход подается строка. Нужно определить длину наибольшей подстроки,
которая не содержит повторяющиеся символы.
"""

s = "ghkjhbkbj"

dct = set()
max_len = 0

if len(s) == 0:
    max_len = 0

for j in range(len(s)):
    for i in range(j, len(s)):
        if s[i] in dct:
            break
        else:
            dct.add(s[i])

    if max_len < len(dct):
        max_len = len(dct)
    dct.clear()

print(max_len)


def findLongest(s):
    maxlen = 0
    for i in range(0, len(s)):
        subs = s[i:]
        chars = set()
        for j, c in enumerate(subs):
            if c in chars:
                break
            else:
                chars.add(c)
        else:
            # add 1 when end of string is reached (no break)
            # handles the case where the longest string is at the end
            j += 1
        if j > maxlen:
            maxlen = j

    return maxlen


print(findLongest(s))
