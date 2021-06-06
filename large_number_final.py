# 33864881
if __name__ == "__main__":
    with open("input.txt") as f:
        try:
            number_quantity = int(f.readline())
            numbers = f.readline().split()
        except Exception as e:
            raise Exception("Неверный формат ввода")


    def radix_add(x):
        x = (x * (4 // len(x) + 1))[:4]
        return x


    numbers.sort(key=radix_add, reverse=True)
    print("".join([str(elem) for elem in numbers]))
