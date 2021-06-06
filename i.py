"""I. Стек - Max
Нужно реализовать класс StackMax, который поддерживает операцию
определения максимума среди всех элементов в стеке.
Класс также должен поддерживать все операции, реализованные в классе Stack, из урока.
При этом в классе StackMax может быть реализовано не более трёх методов.
Стек может содержать только данные типов, поддерживающих операцию сравнения.
Иначе операция поиска максимума будет некорректной.
"""
with open("input.txt") as f:
    n = int(f.readline())
    commands = []
    for i in range(n):
        commands.append(f.readline().split())


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


class StackMax(Stack):
    def __init__(self):
        super().__init__()
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        print("error")

    def get_max(self):
        if not self.isEmpty():
            print(max(self.items))
        else:
            print(None)


stack = StackMax()

for command in commands:
    if command[0] == "get_max":
        stack.get_max()
    if command[0] == "push":
        stack.push(int(command[1]))
    if command[0] == "pop":
        stack.pop()
