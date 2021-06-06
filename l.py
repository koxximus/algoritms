"""L. Скобочная последовательность
Вот какую задачу Тимофей предложил на собеседовании одному из кандидатов.
Если вы с ней еще не сталкивались, то наверняка столкнётесь — она довольно популярная.
Дана скобочная последовательность.
Нужно определить, правильная ли она.
Будем придерживаться такого определения:

- пустая строка — правильная скобочная последовательность;

- правильная скобочная последовательность, взятая в скобки одного типа,
 — правильная скобочная последовательность;

- правильная скобочная последовательность с приписанной слева или справа
правильной скобочной последовательностью — тоже правильная.

На вход подается последовательность из скобок трёх видов: [], (), {}.
Напишите функцию is_correct_bracket_seq, которая принимает на вход скобочную
последовательность и возвращает True, если последовательность правильная, иначе False.

"""
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


s = "["
stack = Stack()


dct = {"(": ")", "[": "]", "{": "}"}


def is_correct_bracket_seq(s):
    for i in s:
        if i in dct.keys():
            stack.push(dct[i])
        elif stack.isEmpty():
            return False
        elif stack.peek() == i:
            stack.pop()
        else:
            return False
    return stack.isEmpty()


print(is_correct_bracket_seq(s))
