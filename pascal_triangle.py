import math


def pascal(x):
    base = [[1]]
    for i in range(x):
        base.append([0])
    for i in range(x - 1):
        for j in range(i + 1):
            base[i + 1].append(0)
        base[i + 1][0] = 1
        base[i + 1][-1] = 1
    base = base[:-1]

    for i in range(2, x):
        for j in range(1, i):
            base[i][j] = base[i - 1][j - i] + base[i - 1][j - i - 1]

    return base

def pascal_char_finder(a):
    list = (pascal(a))[-1]

    result = 0

    for i in list:
        result += len(str(i))

    result += a*2
    return result


def pascal_pyramide_printer(x):
    blank = pascal_char_finder(x) +10
    base = pascal(x+1)
    blank_left = int(blank / 2 +1)
    toplam_blank = (blank_left+2)*2 + 3

    for i in range(len(base)-1):
        blank_right = toplam_blank - math.ceil(blank_left) - pascal_char_finder(i+1) -4

        print("|", int(math.ceil(blank_left)) * " ", base[i], int(blank_right) * " ", "|")

        x = pascal_char_finder(i+1)
        y = pascal_char_finder(i+2)

        blank_left -= (y-x)/2
    return 0

#pascal_pyramide_printer(15)
