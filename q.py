with open("input.txt") as f:
    n = int(f.readline())
    m = int(f.readline())
    commands = []
    for i in range(n):
        commands.append(f.readline().split())


class Deque:
    def __init__(self, m):
        self.items = []
        self.max_size = m
        self.size = 0

    def is_empty(self):
        return self.items == []

    def push_back(self, x):
        if self.size != self.max_size:
            self.items.append(x)
            self.size += 1
        else:
            print("error")

    def push_front(self, x):
        if self.size != self.max_size:
            self.items.insert(0, x)
            self.size += 1
        else:
            print("error")

    def pop_front(self):
        if self.is_empty():
            print("error")
        else:
            x = self.items.pop(0)
            self.size -= 1
            print(x)

    def pop_back(self):
        if self.is_empty():
            print("error")
        else:
            x = self.items.pop()
            self.size -= 1
            print(x)


deque = Deque(m)


for command in commands:
    if command[0] == "push_back":
        deque.push_back(int(command[1]))
    if command[0] == "push_front":
        deque.push_front(int(command[1]))
    if command[0] == "pop_front":
        deque.pop_front()
    if command[0] == "pop_back":
        deque.pop_back()
