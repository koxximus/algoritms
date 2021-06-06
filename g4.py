"""G. Недоалфавит
Кондратий решил взяться за изучение английского языка и устроил конкурс.
Билет на тараканьи бега получит тот, кто напишет самую быструю функцию,
рекурсивно выводящую английский алфавит до заданной буквы включительно.
"""

with open("input.txt") as f:
    n = f.readline()

ascii_lowercase = "abcdefghijklmnopqrstuvwxyz"

def alphabet(n, i=0):
    if ascii_lowercase[i] == n:
        return [a for a in ascii_lowercase[:i+1]]
    return alphabet(n, i+1)


print(" ".join(alphabet(n)))