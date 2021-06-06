"""A. Калькулятор
Задание связано с обратной польской нотацией.
Она используется для парсинга арифметических выражений.
По сравнению с другим приемом, применяемым для данной задачи —
использованием дерева операций, она является более компактной,
так как в ней не используются скобки.
Еще её иногда называют обратной польской записью или постфиксной нотацией.
В постфиксной нотации операнды расположены перед знаками операций.

Пример 1:
3 4 +
будет равно 7, и означает 3 + 4
"""

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return self.value

n1 = Node("1", Node("2", Node("3", Node("4"))))


def hasCycle(head):
    node_set = set()
    while head.next:
        if head in node_set:
            return True
        node_set.add(head)
        head = head.next
    return False


print(hasCycle(n1))
