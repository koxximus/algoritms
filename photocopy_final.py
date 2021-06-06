#посылка 33774519
if __name__ == "__main__":
    with open("input.txt") as f:
        try:
            n = int(f.readline())
            datacenters = sorted([int(elem) for elem in f.readline().split()])
        except Exception as e:
            raise Exception("Неверный формат ввода")

    copy = 0
    while len(datacenters) > 1:
        if datacenters[0] != 0:
            datacenters[0] -= 1
            datacenters[-1] -= 1
            copy += 1
            datacenters.sort()
        else:
            datacenters = datacenters[1:]
    print(copy)
