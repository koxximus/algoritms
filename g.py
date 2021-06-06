"""G. Заботливая мама
Мама Васи хочет знать, что сын планирует делать и когда.
Помогите ей: напишите функцию solution, определяющую индекс
первого вхождения передаваемого ей на вход значения в связном списке,
если значение присутствует.
Внимание: в этой задаче не нужно считывать входные данные.
Нужно написать только функцию, которая принимает на вход голову списка и искомый элемент,
а возвращает целое число — индекс найденного элемента или -1. Ниже дано описание структуры,
которая задаёт вершину списка.
"""
class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item

n4 = Node('forth')
n3 = Node('third', n4)
n2 = Node('second', n3)
n1 = Node('first', n2)


def solution(head, value):
    ids = 0
    if head.value == value:
        return 0
    while head.next_item is not None:
        ids += 1
        head = head.next_item
        if head.value == value:
            return ids
    return -1


print(solution(n1, "fifth"))
