"""E. Бессовестные тараканы
На этот раз нужно определить стартовые номера тараканов с учетом того,
в скольких именно забегах первой и второй категории одновременно они участвовали.
То есть, если таракан со стартовым номером 1 участвовал в двух забегах первой категории,
и в трех забегах второй категории, то номер 1 в ответе должен встречаться два раза.
"""
with open("input.txt") as f:
    len_first_arr = int(f.readline())
    len_second_arr = int(f.readline())
    first_arr = [int(elem) for elem in f.readline().split()]
    second_arr = sorted([int(elem) for elem in f.readline().split()])


def search(arr, bug, left, right):
    mid = left+(right-left)//2
    if arr[mid] == bug:
        arr.remove(bug)
        return bug
    if left >= right:
        return
    if arr[mid] < bug:
        return search(arr, bug, mid+1, right)
    elif arr[mid] > bug:
        return search(arr, bug, left, mid-1)


for bug in first_arr:
    if second_arr:
        bad_bug = search(second_arr, bug, 0, len(second_arr)-1)
        if bad_bug is not None:
            print(bad_bug, end=" ")
