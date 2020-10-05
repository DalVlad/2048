import random
import os
import msvcrt


def control():
    while True:
        entry = msvcrt.getch()
        entry = entry.decode('utf-8')
        entry = str.lower(entry)
        if entry == 'd':
            start_check(1)
            return
        elif entry == 'a':
            start_check(-1)
            return
        elif entry == 'w':
            start_check(2)
            return
        elif entry == 's':
            start_check(-2)
            return


def output():
    for i in range(4):
        print()
        print(end=" ")
        for j in range(4):
            if play_field[i][j] == 0:
                print(end="-    ")
            elif play_field[i][j] > 10:
                print(play_field[i][j], end="   ")
            else:
                print(play_field[i][j], end="    ")
        print("\n")


def number_generator():
    for i in range(101):
        x = random.randint(0, 3)
        y = random.randint(0, 3)
        if play_field[x][y] == 0:
            number = random.randint(0, 100)
            if number <= 90:
                play_field[x][y] = 2
                return
            else:
                play_field[x][y] = 4
                return
    print('YOU DIED')


def shift_field(i, x):
    if x == 1:  # right
        for q in range(4):
            for j in range(4):
                if play_field[i][j] == 0 and j != 0:
                    play_field[i][j] = play_field[i][j - 1]
                    play_field[i][j - 1] = 0
    elif x == -1:  # left
        for q in range(4):
            for j in range(3, -1, -1):
                if play_field[i][j] == 0 and j != 3:
                    play_field[i][j] = play_field[i][j + 1]
                    play_field[i][j + 1] = 0
    elif x == 2:  # up
        for q in range(4):
            for j in range(4):
                if play_field[j][i] == 0 and j != 3:
                    play_field[j][i] = play_field[j + 1][i]
                    play_field[j + 1][i] = 0
    elif x == -2:  # down
        for q in range(4):
            for j in range(3, -1, -1):
                if play_field[j][i] == 0 and j != 0:
                    play_field[j][i] = play_field[j - 1][i]
                    play_field[j - 1][i] = 0


def sum_columns(i, j, w):
    if play_field[w][i] != 0:
        if play_field[w][i] == play_field[j][i]:
            play_field[j][i] *= 2
            play_field[w][i] = 0
            return True


def sum_line(i, j, w):
    if play_field[i][w] != 0:
        if play_field[i][w] == play_field[i][j]:
            play_field[i][j] *= 2
            play_field[i][w] = 0
            return True


def comparison(i, j, x):  # Нахождение пары в строке
    if x == 1:  # right
        for w in range(j - 1, -1, -1):
            if sum_line(i, j, w):
                return
    elif x == -1:  # left
        for w in range(j + 1, 4, 1):
            if sum_line(i, j, w):
                return
    elif x == 2:  # up
        for w in range(j + 1, 4, 1):
            if sum_columns(i, j, w):
                return
    elif x == -2:  # down
        for w in range(j - 1, -1, -1):
            if sum_columns(i, j, w):
                return


def check(i, x):  # Перебор строк
    if x == 1 or x == -2:  # right, down
        for j in range(3, -1, -1):
            comparison(i, j, x)
    elif x == -1 or x == 2:  # left, up
        for j in range(4):
            comparison(i, j, x)


def start_check(x):  # Перебор столбцов
    for i in range(4):
        check(i, x)
        shift_field(i, x)


play_field = [
    [4, 0, 0, 0],
    [2, 0, 0, 0],
    [2, 0, 0, 0],
    [0, 0, 0, 0]
]
for f in range(4):
    number_generator()

while True:
    number_generator()
    output()
    control()
    os.system("cls")
