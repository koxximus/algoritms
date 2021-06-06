"""G. Закручивающаяся спираль
Волшебная фея отправила Гоше послание. Чтобы никто не смог перехватить сообщение,
фея его закодировала. Послание записано в матрице по спирали,
начиная с левого верхнего угла вправо.
Помогите Гоше прочитать сообщение.
"""
with open("input.txt") as f:
    n = int(f.readline())
    m = int(f.readline())
    matrix = []
    for i in range(n):
        matrix.append(f.readline().split())
A = 1
i, j = 0, 0
N = n * m

for p in range(m//2+1):
    for right in range(p, m-1-p):
        if A > N:
            break
        else:
            print(matrix[i][j], end=" ")
            A += 1
            j += 1
    for down in range(p, n-1-p):
        if A > N:
            break
        else:
            print(matrix[i][j], end=" ")
            A += 1
            i += 1
    for left in range(p, m-1-p):
        if A > N:
            break
        else:
            print(matrix[i][j], end=" ")
            A += 1
            j -= 1
    for up in range(p, n-1-p):
        if A > N:
            break
        else:
            print(matrix[i][j], end=" ")
            A += 1
            i -= 1
    i += 1
    j += 1

if m == n and m%2==1:
    print(matrix[m//2][n//2])

"""
def spiralOrder(matrix):
    result = []
    while matrix:
        result.extend(matrix.pop(0))
        matrix = list(zip(*matrix))[::-1]
    return result
matrix = [
    [1,   2,  3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10,  9,  8, 7],
]
print(" ".join(str(x) for x in spiralOrder(matrix)))
"""