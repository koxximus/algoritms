"""J. Стек - MaxEffective
Реализуйте класс StackMaxEffective, поддерживающий операцию
определения максимума среди элементов в стеке.
Сложность операции должна быть O(1).
Для пустого стека операция должна возвращать None.
При этом push и pop также должны выполняться за константное время.
"""

with open("input.txt") as f:
    n = int(f.readline())
    commands = []
    for i in range(n):
        commands.append(f.readline().split())


class StackMaxEffective:
    def __init__(self):
        self.items = []
        self.max_items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        if self.isEmpty():
            self.items.append(item)
            self.max_items.append(item)
        else:
            self.items.append(item)
            if item > self.max_items[-1]:
                self.max_items.append(item)
            else:
                self.max_items.append(self.max_items[-1])

    def pop(self):
        if not self.isEmpty():
            return self.items.pop(), self.max_items.pop()
        print("error")

    def get_max(self):
        if not self.isEmpty():
            print(self.max_items[-1])
        else:
            print(None)


stack = StackMaxEffective()

for command in commands:
    if command[0] == "get_max":
        stack.get_max()
    if command[0] == "push":
        stack.push(int(command[1]))
    if command[0] == "pop":
        stack.pop()
