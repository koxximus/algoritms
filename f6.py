def solution(root, path=[]):
    q = [root]
    level = 0

    while q:
        count = len(q)
        cur_level = level + 1

        while count > 0:

            temp = q.pop(0)

            if temp.left:
                q.append(temp.left)

            if temp.right:
                q.append(temp.right)

            if cur_level > level:
                path.append(temp.value)

            count -= 1
            cur_level -= 1

        level += 1

    return path