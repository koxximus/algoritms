"""M. Очередь
Перед Тимофеем стоит задача написать несколько реализаций собственной очереди,
так как доступные на рынке варианты для проекта не подходят.
Требования к первой вот такие: класс должен называться MyQueue(),
поддерживать операции добавления, удаления, получения элемента,
определение текущего размера, и метод, показывающий,
пуста ли очередь или нет. Реализована структура данных должна быть на основе массива.
"""
with open("input.txt") as f:
    n = int(f.readline())
    commands = []
    for i in range(n):
        commands.append(f.readline().split())


class MyQueue:
    def __init__(self):
        self.queue = []

    def size(self):
        print(len(self.queue))

    def is_empty(self):
        return self.queue == []

    def push(self, x):
        self.queue.append(x)

    def pop(self):
        if self.is_empty():
            print(None)
        else:
            x = self.queue.pop(0)
            print(x)

    def peek(self):
        if self.is_empty():
            print(None)
        else:
            print(self.queue[0])


queue = MyQueue()


for command in commands:
    if command[0] == "size":
        queue.size()
    if command[0] == "push":
        queue.push(int(command[1]))
    if command[0] == "pop":
        queue.pop()
    if command[0] == "peek":
        queue.peek()

