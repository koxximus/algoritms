"""N. Ограниченная очередь
Далее Тимофею нужно написать класс MyQueueSized(), который принимает параметр max_size,
означающий максимально допустимое количество элементов в очереди.
"""
with open("input.txt") as f:
    n = int(f.readline())
    m = int(f.readline())
    commands = []
    for i in range(n):
        commands.append(f.readline().split())


class MyQueueSized:
    def __init__(self, m):
        self.queue = [None for _ in range(m)]
        self.max_size = m
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, x):
        if self.size != self.max_size:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_size
            self.size += 1
        else:
            print("error")

    def pop(self):
        if self.is_empty():
            print(None)
        else:
            x = self.queue[self.head]
            self.queue[self.head] = None
            self.head = (self.head + 1) % self.max_size
            self.size -= 1
            print(x)

    def peek(self):
        if self.is_empty():
            print(None)
        else:
            print(self.queue[self.head])


queue = MyQueueSized(m)


for command in commands:
    if command[0] == "size":
        print(queue.size)
    if command[0] == "push":
        queue.push(int(command[1]))
    if command[0] == "pop":
        queue.pop()
    if command[0] == "peek":
        queue.peek()
