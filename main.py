def output():
    for i in range(4):
        print()
        for j in range(4):
            if play_field[i][j] == 0:
                print(end="- ")
            else:
                print(play_field[i][j], end=" ")


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


def comparison(i, j, x):  # Нахождение пары в строке
    if x == 1:  # right
        for w in range(j - 1, -1, -1):
            if play_field[i][w] != 0 and play_field[i][w] == play_field[i][j]:
                play_field[i][j] *= 2
                play_field[i][w] = 0
                return
            else:
                return
    elif x == -1:  # left
        for w in range(j + 1, 4, 1):
            if play_field[i][w] != 0 and play_field[i][w] == play_field[i][j]:
                play_field[i][j] *= 2
                play_field[i][w] = 0
                return
            else:
                return
    elif x == 2:  # up
        for w in range(j + 1, 4, 1):
            if play_field[w][i] != 0 and play_field[w][i] == play_field[j][i]:
                play_field[j][i] *= 2
                play_field[w][i] = 0
                return
            else:
                return
    elif x == -2:  # down
        for w in range(j - 1, 4, 1):
            if play_field[w][i] != 0 and play_field[w][i] == play_field[j][i]:
                play_field[j][i] *= 2
                play_field[w][i] = 0
                return
            else:
                return


def check(i, x):  # Перебор строк
    if x == 1:  # right
        for j in range(3, -1, -1):
            if play_field[i][j] != 0 and j != 0:
                comparison(i, j, x)
    elif x == -1:  # left
        for j in range(4):
            if play_field[i][j] != 0 and j != 3:
                comparison(i, j, x)
    elif x == 2:  # up
        for j in range(4):
            if play_field[j][i] != 0 and j != 3:
                comparison(i, j, x)
    elif x == -2:  # down
        for j in range(3, -1, -1):
            if play_field[j][i] != 0 and j != 0:
                comparison(i, j, x)


def start_check(x):  # Перебор столбцов
    if x == 1:  # right
        for i in range(4):
            check(i, x)
            shift_field(i, x)
    elif x == -1:  # left
        for i in range(4):
            check(i, x)
            shift_field(i, x)
    elif x == 2:    # up
        for i in range(4):
            check(i, x)
            shift_field(i, x)
    elif x == -2:   # down
        for i in range(4):
            check(i, x)
            shift_field(i, x)


# x = int(input())

play_field = [
    [2, 2, 2, 4],
    [2, 4, 4, 2],
    [4, 4, 2, 4],
    [2, 2, 4, 4]
]

while True:

    output()

    control = str.lower(input())
    if control == 'd':
        start_check(1)
    elif control == 'a':
        start_check(-1)
    elif control == 'w':
        start_check(2)
    elif control == 's':
        start_check(-2)
