"""K. Уникальный Стек
Реализуйте класс StackSet, который хранит только уникальные элементы.
При этом операция добавления элемента в стек должна выполняться за O(1).
"""

with open("input.txt") as f:
    n = int(f.readline())
    commands = []
    for i in range(n):
        commands.append(f.readline().split())


class StackSet:
    def __init__(self):
        self.items = set()
        self.list_items = []

    def push(self, item):
        if item not in self.items:
            self.items.add(item)
            self.list_items.append(item)

    def isEmpty(self):
        return self.list_items == []

    def pop(self):
        if self.isEmpty():
            print("error")
        else:
            elem = self.list_items.pop()
            return self.items.remove(elem)

    def peek(self):
        if self.isEmpty():
            print("error")
        else:
            print(self.list_items[len(self.list_items) - 1])

    def size(self):
        print(len(self.list_items))


stack = StackSet()

for command in commands:
    if command[0] == "push":
        stack.push(int(command[1]))
    elif command[0] == "pop":
        stack.pop()
    elif command[0] == "size":
        stack.size()
    elif command[0] == "peek":
        stack.peek()
