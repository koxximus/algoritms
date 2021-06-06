"""F. Нелюбимое дело
Вася размышляет, что бы такое из списка не делать.
Но, кажется, все пункты очень важные!
Вася решает загадать число и удалить дело, которое идёт под этим номером.
Список дел представлен в виде односвязного списка. Напишите функцию solution,
которая принимает на вход голову списка и номер удаляемого
дела и возвращает голову обновлённого списка.
Внимание: в этой задаче не нужно считывать входные данные.
Нужно написать только функцию, которая принимает на вход голову списка и
номер удаляемого элемента и возвращает голову обновленного списка.
 Ниже дано описание структуры, которая задаёт вершину списка.
"""
class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item
    def __str__(self):
        return self.value

n4 = Node('forth')
n3 = Node('third', n4)
n2 = Node('second', n3)
n1 = Node('first', n2)


def solution(head, index):
    ids = 0
    if index == 0:
        head = head.next_item
        return head
    node = head
    while ids < index-1:
        node = node.next_item
        ids += 1
    tmp = node.next_item
    node.next_item = tmp.next_item
    return head



print(solution(n1, 2))

