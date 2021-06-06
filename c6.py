"""C. Генеалогическое древо
Гуляя по вилле Кондратия, ребята нашли генеалогическое древо его семьи.
Им стало интересно, сколько лет прожили члены семьи разных поколений.
Помогите ребятам это выяснить.
"""

def solution(root, path=[]):
    q = [root]
    tmp = []

    while q:
        count = len(q)

        while count > 0:

            temp = q.pop(0)

            tmp += [temp.value]

            if temp.left:
                q.append(temp.left)

            if temp.right:
                q.append(temp.right)

            count -= 1
        path.append(tmp)
        tmp = []
    return path
