"""H. Возрастающий подмассив
Во сне Гоша долго играл в игру Лампочка. Он то выигрывал, то проигрывал.
Ему стало интересно,
сколько максимум партий подряд он получал большее количество очков,
чем в предыдущей.
"""

with open("input.txt") as f:
    n = int(f.readline())
    games = list(map(int, f.readline().split()))

result = [1,]
maximum = 1

for i in range(0, n-1):
    if games[i] < games[i+1]:
        result.append(games[i])
    else:
        if len(result) > maximum:
            maximum = len(result)
        result.clear()
        result.append(1)


print(max(len(result), maximum))













