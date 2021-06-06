"""H. Все наоборот
Вася решил запутать маму —– делать дела в обратном порядке.
Список его дел теперь хранится в двусвязном списке.
Напишите функцию, которая вернёт список в обратном порядке.
Внимание: в этой задаче не нужно считывать входные данные.
Нужно написать только функцию, которая принимает на вход голову двусвязного списка
и возвращает голову перевернутого списка. Ниже дано описание структуры,
которая задаёт вершину списка.
"""
class Cell:
    def __init__(self, value):
        self.value = value

    def set_prev_and_next(self, prev, next):
        self.prev = prev
        self.next = next

    def __str__(self):
        return self.value


A = Cell("1")
B = Cell("2")
C = Cell("3")
D = Cell("4")
E = Cell("5")

A.set_prev_and_next(None, B)
B.set_prev_and_next(A, C)
C.set_prev_and_next(B, D)
D.set_prev_and_next(C, E)
E.set_prev_and_next(D, None)


def solution(head):
    while head.next is not None:
        head = head.next

    new_head = head
    while head.prev is not None:

        node = head.prev

        head.prev = head.next
        head.next = node

        head = node

    return new_head


print(solution(A))