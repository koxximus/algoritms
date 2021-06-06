"""B. Сбалансированное дерево
Гоше очень понравилось слушать рассказ Тимофея про деревья.
Особенно часть про сбалансированные деревья.
Он решил написать функцию, которая определяет, сбалансировано ли дерево.
Дерево считается сбалансированным,
если левое и правое поддеревья каждого узла отличаются по высоте не больше, чем на один.
"""


def height(root):
    if root is None:
        return 0

    return 1 + max(height(root.left), height(root.right))


def solution(root):
    if root is None:
        return True

    if (abs(height(root.left) - height(root.right)) < 2 and
            solution(root.left) and
            solution(root.right)):
        return True
    else:
        return False
