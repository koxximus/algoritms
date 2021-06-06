"""R. Список дел (старая)
Васе нужно распечатать свой список дел на сегодня.
Помогите ему: напишите функцию print_linked_list,
которая печатает по очереди значения всех элементов в списке.
На вход функция принимает голову списка.
"""
with open("input.txt") as f:
    n = int(f.readline())
    deals = f.read().splitlines()


class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item

    def __str__(self):
        return self.value


node = None

for i in range(n):
    if not node:
        node = Node(deals[i])
        node.next_item = None
    else:
        tmp = node
        node = Node(deals[i])
        node.next_item = tmp


def solution(head):
    while head.next_item is not None:
        print(head)
        head = head.next_item
    print(head)


solution(node)
