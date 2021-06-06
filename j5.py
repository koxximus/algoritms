"""J. Относительная сортировка
Кондратий ввел новый метод сортировки - Относительная сортировка.
Идея метода следующая. С помощью образца - массива уникальных чисел, задается порядок.
В соответствии с этим порядком и должны сортироваться числа.
Но метод еще требует доработки. Пока не известно, как сортировать числа,
которые не входят в образец.
Так что такие числа нужно выводить в конце в соответствии со стандартной сортировкой.
"""
with open("input.txt") as f:
    len_nums = int(f.readline())
    nums = f.readline().split()
    len_pattern = int(f.readline())
    pattern = f.readline().split()

count_nums = [0 for _ in range(len_pattern)]

for num in nums[::-1]:
    if num in pattern:
        count_nums[pattern.index(num)] += 1
        nums.remove(num)

for i in range(len_pattern):
    print((pattern[i]+" ") * count_nums[i], end="")
print(" ".join(sorted(nums, key=int)))
