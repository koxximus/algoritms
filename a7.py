with open("input.txt") as f:
    num = f.readline()

def square(num):
    print(num)
    if num == "1":
        return True
    if num == "0":
        return False
    if num == "145":
        return False
    num = sum(int(elem)**2 for elem in num)
    return square(str(num))

print(square(num))
