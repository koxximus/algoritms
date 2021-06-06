"""D. Дерево - анаграмма
Кондратий приказал найти в его лесу дерево - анаграмму.
Гоша и Алла отправились на поиски. Помогите ребятам определить,
является ли дерево, которое они нашли деревом - анаграммой?
Дерево является анаграммой, если оно симметричное относительно своего центра.
"""

def solution(root):
    if root is None:
        return True

    if not root.left and not root.right:
        return True

    q = []
    q.append(root)
    q.append(root)

    while q:
        templ = q.pop(0)
        tempr = q.pop(0)
        if templ.value != tempr.value:
            return False

        if templ.left and tempr.right:
            q.append(templ.left)
            q.append(tempr.right)
        elif templ.left or tempr.right:
            return False

        if templ.right and tempr.left:
            q.append(templ.right)
            q.append(tempr.left)
        elif templ.right or tempr.left:
            return False

    return True


#2
def simetric(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is not None and root2 is not None:
        if root1.value == root2.value:
            return simetric(root1.left, root2.right) and simetric(root1.right, root2.left)
    return False

def solution(root):
    return simetric(root, root)
