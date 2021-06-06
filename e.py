"""E. Список дел
Васе нужно распечатать свой список дел на сегодня.
Помогите ему: напишите функцию, которая печатает все его дела.
Известно, что дел у Васи не больше 5000.
Внимание: в этой задаче не нужно считывать входные данные.
Нужно написать только функцию, которая принимает на вход голову
списка и печатает его элементы. Ниже дано описание структуры,
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


def solution(head):
    while head.next_item is not None:
        print(head.value)
        head = head.next_item
    print(head.value)


solution(n1)
