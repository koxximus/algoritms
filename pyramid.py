# 34112065
def split_array(arr):
    kondratiy = []
    others = []
    for num, player in enumerate(arr[::-1]):
        if not set("kondratiy").issubset(player[1]):
            others.append([num] + player)
        else:
            kondratiy.append([num] + player)
    return kondratiy, others


def compare(a, b):
    if (a[1] > b[1] or
            a[1] == b[1] and a[2] < b[2] or
            a[1] == b[1] and a[2] == b[2] and a[0] < b[0]):
        return True


def heapify(arr, n, i):
    smallest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and compare(arr[i], arr[l]):
        smallest = l
    if r < n and compare(arr[smallest], arr[r]):
        smallest = r
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, n, smallest)


def heap_sort(arr):
    n = len(arr)

    for i in range(n, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr


if __name__ == "__main__":
    with open("input.txt") as f:
        q_players = int(f.readline())
        players = []
        for _ in range(q_players):
            string = f.readline().split()
            players += [[sum(int(elem) for elem in string[1:] if int(elem) > 0)] + string]

    kondratiy_array, other_array = split_array(players)
    result = kondratiy_array + heap_sort(other_array)
    for player in result:
        print(" ".join(player[2:]))
