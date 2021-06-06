#посылка 33697633
with open("input.txt") as f:
    elems = f.readline().split()


def calc(elems):
    stack = []
    signs = set("+-*/")
    for elem in elems:
        if elem not in signs:
            stack.append(int(elem))
        else:
            y = stack.pop()
            x = stack.pop()
            if elem == "+": result = x + y
            if elem == "-": result = x - y
            if elem == "*": result = x * y
            if elem == "/": result = x // y
            stack.append(result)
    return stack[-1]


print(calc(elems))
