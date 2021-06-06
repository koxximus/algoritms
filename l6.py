k = 10
simple = [1, 2, 3, 5]
kondranachi = [1, 2, 3, 5]
i = 1
while len(kondranachi) < k:
    for j in range(1, len(simple)):
        next_kond = simple[j]*kondranachi[i]
        kondranachi.append((next_kond))
        kondranachi.sort()
    i += 1

print(sorted(kondranachi))