"""I. Дерево поиска
Гоша понял, что такое дерево поиска, и захотел написать функцию,
которая определяет, является ли заданное дерево деревом поиска.
Значения в левом поддереве должны быть строго меньше,
в правом - строго больше значения в узле.
Помогите Гоше с реализацией.
"""

INT_MAX = 4294967296
INT_MIN = -4294967296


def isbst(root, mini, maxi):
    if root is None:
        return True
    if root.value < mini or root.value > maxi:
        return False
    return isbst(root.left, mini, root.value - 1) and isbst(root.right, root.value + 1, maxi)


def solution(root):
    return isbst(root, INT_MIN, INT_MAX)


#2
def max_val(root, path=[]):
    path += [root.value]
    if root.left:
        max_val(root.left)
    if root.right:
        max_val(root.right)
    return max(path)


def min_val(root, path=[]):
    path += [root.value]
    if root.left:
        min_val(root.left)
    if root.right:
        min_val(root.right)
    return min(path)


def solution(root):
    if root.left is None and root.right is None:
        return True
    if root.left and max_val(root.left) >= root.value:
        return False
    if root.right and min_val(root.right) <= root.value:
        return False

    return True
