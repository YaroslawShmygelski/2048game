import random
import numpy as np


def pretty_print(gametab):
    print("-" * 100)
    for row in gametab:
        print(*row)
    print("-" * 100)


def get_number_from_index(row, col):
    return row * 4 + (col + 1)


def get_index_from_number(num):
    row = (num - 1) // 4
    col = (num - 1) % 4
    return row, col


def get_empty_list(gametab):
    empty_list = []
    for row in range(4):
        for col in range(4):
            if gametab[row][col] == 0:
                empty_list.append(get_number_from_index(row, col))

    return empty_list


def get_2_or_4(mas, x, y):
    if (random.random() <= 0.9):
        mas[x][y] = 2
    else:
        mas[x][y] = 4
    return mas


def is_zero_in_mas(mas):
    for i in mas:
        for j in i:
            if j == 0:
                return True
    return False


def move_left(mas):
    for row in mas:
        while 0 in row:
            row.remove(0)
        while len(row) != 4:
            row.append(0)
    for i in range(4):
        for j in range(3):
            if (mas[i][j] == mas[i][j + 1]):
                mas[i][j] *= 2

                del mas[i][j + 1]
                mas[i].append(0)

    return mas


def move_right(mas):
    for row in mas:
        while 0 in row:
            row.remove(0)
        while len(row) != 4:
            row.insert(0, 0)
    for i in range(4):
        for j in range(3, 0, -1):
            if (mas[i][j] == mas[i][j - 1] and mas[i][j] != 0):
                mas[i][j] *= 2

                del mas[i][j - 1]
                mas[i].insert(0, 0)

    return mas


def move_up(mas):
    arr_main = []
    for i in range(4):
        arr = []
        for col in mas:
            arr.append(col[i])
        arr_main.append(arr)
    mas = arr_main

    for row in mas:
        while 0 in row:
            row.remove(0)
        while len(row) != 4:
            row.append(0)
    for i in range(4):
        for j in range(3):
            if (mas[i][j] == mas[i][j + 1]):
                mas[i][j] *= 2
                del mas[i][j + 1]
                mas[i].append(0)

    trans_mas = [[mas[j][i] for j in range(4)] for i in range(4)]
    mas = trans_mas
    return mas


def move_down(mas):
    arr_main = []
    for i in range(4):
        arr = []
        for col in mas:
            arr.append(col[i])
        arr_main.append(arr)
    mas = arr_main

    for row in mas:
        while 0 in row:
            row.remove(0)
        while len(row) != 4:
            row.insert(0, 0)
    for i in range(4):
        for j in range(3, 0, -1):
            if (mas[i][j] == mas[i][j - 1] and mas[i][j] != 0):
                mas[i][j] *= 2
                del mas[i][j - 1]
                mas[i].insert(0, 0)

    trans_mas = [[mas[j][i] for j in range(4)] for i in range(4)]
    mas = trans_mas
    return mas


def can_move(mas):
    for i in range(3):
        for j in range(3):
            if mas[i][j] == mas[i][j + 1] or mas[i][j] == mas[i + 1][j]:
                return True
    return False


def total(mas):
    sum = np.sum(mas)
    return sum


def max_element(mas):
    max = np.max(mas)
    return max

def zero_values():
    mas = [[0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0],
           ]
    value1=0
    value2=0
    return mas, value1, value2