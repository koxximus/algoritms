"""P. Списочная очередь
Любимый вариант очереди Тимофея - очередь, написанная с использованием связного списка.
Помогите ему с реализацией.
Очередь должна поддерживать методы get, put, size.
"""

with open("input.txt") as f:
    n = int(f.readline())
    commands = []
    for i in range(n):
        commands.append(f.readline().split())


class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


class MyQueue:
    def __init__(self):
        self.length = 0
        self.head = None

    def size(self):
        print(self.length)

    def is_empty(self):
        return self.length == 0

    def put(self, x):
        node = Node(x)
        node.next_item = None
        if self.is_empty():
            self.head = node
        else:
            last = self.head
            while last.next_item:
                last = last.next_item
            last.next_item = node
        self.length += 1

    def get(self):
        if self.is_empty():
            print("error")
        else:
            tmp = self.head
            self.head = tmp.next_item
            self.length -= 1
            print(tmp.value)


queue = MyQueue()


for command in commands:
    if command[0] == "size":
        queue.size()
    if command[0] == "put":
        queue.put(int(command[1]))
    if command[0] == "get":
        queue.get()
